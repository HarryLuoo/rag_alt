#!/usr/bin/env python3
"""
Two-Layer Agentic Knowledge System Prototype
============================================

This script implements a two-layer agentic system using OpenRouter API:
- Layer 1: Agent A (Frontend Gatekeeper) - decides when to delegate
- Layer 2: Agent R_i (Reference Agents) - dynamically instantiated for specific knowledge chunks

Requirements:
- Python 3.7+
- langchain-openai
- OpenRouter API key

Usage:
1. Set your OpenRouter API key in the OPENROUTER_API_KEY variable
2. Run the script
3. Use 'load <filename.md>' to load a markdown document
4. Ask questions and the system will route them appropriately
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Try to import API key from config file
try:
    from config import OPENROUTER_API_KEY
except ImportError:
    OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY_HERE"
    print("Warning: config.py not found. Please create it with your OpenRouter API key.")

# =============================================================================
# CONFIGURATION
# =============================================================================

# OpenRouter configuration
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Model configurations
AGENT_A_MODEL = "google/gemma-3n-e2b-it:free"  # Lightweight for Agent A
AGENT_R_MODEL = "google/gemma-3-12b-it:free"  # More capable for Agent R_i

# Directory and file paths
DIRECTORY_FILE = "directory.json"
CHUNKS_DIR = "chunks"

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def ensure_directories():
    """Create necessary directories if they don't exist."""
    Path(CHUNKS_DIR).mkdir(exist_ok=True)

def load_directory() -> Dict:
    """Load the knowledge directory from JSON file."""
    if not os.path.exists(DIRECTORY_FILE):
        return {}
    
    try:
        with open(DIRECTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print(f"Warning: Could not load {DIRECTORY_FILE}. Starting with empty directory.")
        return {}

def save_directory(directory: Dict):
    """Save the knowledge directory to JSON file."""
    try:
        with open(DIRECTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(directory, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving directory: {e}")

def create_directory_summary(directory: Dict) -> str:
    """Create a lean JSON summary for Agent A's prompt (only section_id and description)."""
    summary = {}
    for section_id, details in directory.items():
        summary[section_id] = {"description": details["description"]}
    return json.dumps(summary, ensure_ascii=False)

# =============================================================================
# KNOWLEDGE BASE PARSING
# =============================================================================

def parse_markdown_document(file_path: str) -> Tuple[Dict, int]:
    """
    Parse a markdown document into larger chunks based primarily on H1 headings.
    This creates bigger, more contextual chunks rather than fine-grained sections.
    
    Args:
        file_path: Path to the markdown file
        
    Returns:
        Tuple of (directory_entries, chunk_count)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}, 0
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return {}, 0

    # Split content primarily by H1 headings (# heading) to create larger chunks
    h1_sections = re.split(r'^# ', content, flags=re.MULTILINE)
    
    directory_entries = {}
    chunk_count = 0
    
    # Create a unique prefix based on the filename
    file_prefix = Path(file_path).stem.replace(' ', '_').replace('-', '_')
    
    # Process each H1 section as a complete chunk (including all H2 subsections)
    for h1_idx, h1_section in enumerate(h1_sections):
        if not h1_section.strip():
            continue
            
        if h1_idx == 0:
            # Skip the content before the first H1 heading (usually just title/intro)
            continue
            
        # Extract H1 heading and all content (including H2 subsections)
        h1_lines = h1_section.split('\n', 1)
        h1_heading = h1_lines[0].strip()
        h1_content = h1_lines[1] if len(h1_lines) > 1 else ""
        
        # Create section ID
        section_id = f"{file_prefix}_chapter_{h1_idx}"
        
        # Save the entire H1 section (with all H2 subsections) as one chunk
        chunk_file = f"{CHUNKS_DIR}/{section_id}.txt"
        chunk_content = f"# {h1_heading}\n{h1_content}"
        
        try:
            with open(chunk_file, 'w', encoding='utf-8') as f:
                f.write(chunk_content.strip())
                
            # Add to directory with descriptive title
            directory_entries[section_id] = {
                "description": h1_heading,
                "chunk_file": chunk_file
            }
            chunk_count += 1
            
        except Exception as e:
            print(f"Error saving chunk {section_id}: {e}")
    
    # If no H1 headings found, fall back to H2 chunking but group them more
    if chunk_count == 0:
        print(f"No H1 headings found in {file_path}, trying H2 grouping...")
        h2_sections = re.split(r'^## ', content, flags=re.MULTILINE)
        
        # Group H2 sections into larger chunks (2-3 sections per chunk)
        sections_per_chunk = 2
        current_chunk_sections = []
        current_chunk_titles = []
        
        for i, section in enumerate(h2_sections[1:], 1):  # Skip content before first H2
            if not section.strip():
                continue
                
            # Extract heading and content
            lines = section.split('\n', 1)
            heading = lines[0].strip()
            section_content = lines[1] if len(lines) > 1 else ""
            
            current_chunk_sections.append(f"## {heading}\n{section_content}")
            current_chunk_titles.append(heading)
            
            # Create chunk when we have enough sections or reached the end
            if len(current_chunk_sections) >= sections_per_chunk:
                section_id = f"{file_prefix}_group_{len(directory_entries) + 1}"
                chunk_file = f"{CHUNKS_DIR}/{section_id}.txt"
                
                # Combine multiple H2 sections into one chunk
                chunk_content = "\n\n".join(current_chunk_sections)
                
                # Create a descriptive title combining the section titles
                if len(current_chunk_titles) == 1:
                    description = current_chunk_titles[0]
                else:
                    description = f"{current_chunk_titles[0]} and {current_chunk_titles[-1]}"
                
                try:
                    with open(chunk_file, 'w', encoding='utf-8') as f:
                        f.write(chunk_content.strip())
                        
                    directory_entries[section_id] = {
                        "description": description,
                        "chunk_file": chunk_file
                    }
                    chunk_count += 1
                    
                except Exception as e:
                    print(f"Error saving chunk {section_id}: {e}")
                
                # Reset for next chunk
                current_chunk_sections = []
                current_chunk_titles = []
        
        # Handle remaining sections if any
        if current_chunk_sections:
            section_id = f"{file_prefix}_group_{len(directory_entries) + 1}"
            chunk_file = f"{CHUNKS_DIR}/{section_id}.txt"
            
            chunk_content = "\n\n".join(current_chunk_sections)
            
            if len(current_chunk_titles) == 1:
                description = current_chunk_titles[0]
            else:
                description = f"{current_chunk_titles[0]} and others"
            
            try:
                with open(chunk_file, 'w', encoding='utf-8') as f:
                    f.write(chunk_content.strip())
                    
                directory_entries[section_id] = {
                    "description": description,
                    "chunk_file": chunk_file
                }
                chunk_count += 1
                
            except Exception as e:
                print(f"Error saving chunk {section_id}: {e}")
    
    return directory_entries, chunk_count

def load_document(file_path: str) -> bool:
    """
    Load and parse a markdown document into the knowledge base.
    
    Args:
        file_path: Path to the markdown file
        
    Returns:
        True if successful, False otherwise
    """
    print(f"Loading document: {file_path}")
    
    # Parse the document
    new_entries, chunk_count = parse_markdown_document(file_path)
    
    if chunk_count == 0:
        print("No valid sections found in the document.")
        return False
    
    # Load existing directory and merge
    directory = load_directory()
    directory.update(new_entries)
    
    # Save updated directory
    save_directory(directory)
    
    print(f"Successfully loaded {chunk_count} sections from '{file_path}'")
    print(f"Total sections in knowledge base: {len(directory)}")
    
    return True

# =============================================================================
# AGENT INITIALIZATION
# =============================================================================

def initialize_openrouter_client(model: str) -> ChatOpenAI:
    """Initialize ChatOpenAI client for OpenRouter."""
    if OPENROUTER_API_KEY == "YOUR_OPENROUTER_API_KEY_HERE":
        raise ValueError("Please set your OpenRouter API key in the OPENROUTER_API_KEY variable")
    
    return ChatOpenAI(
        model=model,
        openai_api_base=OPENROUTER_BASE_URL,
        openai_api_key=OPENROUTER_API_KEY,
        temperature=0.1
    )

# =============================================================================
# AGENT A DECISION LOGIC
# =============================================================================

def create_agent_a_prompt(user_query: str, directory_summary: str) -> str:
    """Create the prompt for Agent A."""
    return f"""You are Agent A, a helpful but concise assistant with limited knowledge. Your available reference material is summarized in this directory: {directory_summary}

For the user's query: "{user_query}"

First, determine if you can answer confidently on your own. Rate your confidence from 1 to 10.
If your confidence is 8 or higher, answer directly.
If your confidence is below 8, you must consult reference material. Identify the most relevant section(s) from the directory to answer the query.

IMPORTANT: Look for queries that require information from multiple sources:

When in doubt, select multiple relevant sections rather than just one.

Respond ONLY in JSON format.
- If answering directly, use: {{"needs_reference": false, "answer": "Your direct answer here."}}
- If delegating to ONE section, use: {{"needs_reference": true, "scope": ["directory_section_id"], "sub_query": "A precise question for the reference agent.", "reason": "Why you need the reference."}}
- If delegating to MULTIPLE sections, use: {{"needs_reference": true, "scope": ["section_id_1", "section_id_2", "section_id_3"], "sub_query": "A precise question for the reference agent.", "reason": "Why you need multiple references."}}"""

def query_agent_a(user_query: str, directory: Dict) -> Dict:
    """
    Query Agent A to decide whether to answer directly or delegate.
    
    Args:
        user_query: The user's question
        directory: The knowledge directory
        
    Returns:
        Agent A's decision as a dictionary
    """
    # Create directory summary (lean JSON with only section_id and description)
    directory_summary = create_directory_summary(directory)
    
    # Create the prompt
    system_prompt = create_agent_a_prompt(user_query, directory_summary)
    
    try:
        # Initialize Agent A client
        agent_a = initialize_openrouter_client(AGENT_A_MODEL)
        
        # Get response
        messages = [SystemMessage(content=system_prompt)]
        response = agent_a.invoke(messages)
        
        # Parse JSON response
        response_content = response.content.strip()
        
        # Extract JSON from response (in case there's extra text)
        json_match = re.search(r'\{.*\}', response_content, re.DOTALL)
        if json_match:
            response_content = json_match.group()
        
        decision = json.loads(response_content)
        return decision
        
    except json.JSONDecodeError as e:
        print(f"Error: Agent A returned malformed JSON. Please rephrase your query.")
        print(f"Raw response: {response_content}")
        return {"error": "malformed_json"}
    except Exception as e:
        print(f"Error querying Agent A: {e}")
        return {"error": str(e)}

# =============================================================================
# AGENT R_i REFERENCE LOGIC
# =============================================================================

def create_agent_r_prompt(chunk_text: str, sub_query: str) -> str:
    """Create the prompt for Agent R_i."""
    return f"""You are a meticulous expert tasked with answering a question based ONLY on the following text. Do not use any outside knowledge.

Text: {chunk_text}

Question: {sub_query}

Please provide a detailed, accurate answer based solely on the information provided in the text above."""

def create_multi_agent_r_prompt(combined_chunks: str, sub_query: str) -> str:
    """Create the prompt for Agent R_i when processing multiple chunks."""
    return f"""You are a meticulous expert tasked with answering a question based ONLY on the following reference materials. Do not use any outside knowledge.

Reference Materials:
{combined_chunks}

Question: {sub_query}

Please provide a comprehensive answer by analyzing all the provided reference materials. Synthesize information from different sections when relevant, but base your answer strictly on the text provided above."""

def query_agent_r_single(chunk_file: str, sub_query: str) -> str:
    """
    Query Agent R_i with a single knowledge chunk.
    
    Args:
        chunk_file: Path to the chunk file
        sub_query: The specific question for Agent R_i
        
    Returns:
        Agent R_i's response
    """
    try:
        # Load the chunk content
        with open(chunk_file, 'r', encoding='utf-8') as f:
            chunk_text = f.read()
        
        # Create the prompt
        system_prompt = create_agent_r_prompt(chunk_text, sub_query)
        
        # Initialize Agent R_i client
        agent_r = initialize_openrouter_client(AGENT_R_MODEL)
        
        # Get response
        messages = [SystemMessage(content=system_prompt)]
        response = agent_r.invoke(messages)
        
        return response.content.strip()
        
    except FileNotFoundError:
        return f"Error: Chunk file '{chunk_file}' not found."
    except Exception as e:
        return f"Error querying Agent R_i: {e}"

def query_agent_r_multiple(chunk_files: List[str], sub_query: str, directory: Dict) -> str:
    """
    Query Agent R_i with multiple knowledge chunks.
    
    Args:
        chunk_files: List of paths to chunk files
        sub_query: The specific question for Agent R_i
        directory: The knowledge directory for section descriptions
        
    Returns:
        Agent R_i's response
    """
    try:
        # Load and combine all chunk contents
        combined_chunks = ""
        
        for i, chunk_file in enumerate(chunk_files, 1):
            try:
                with open(chunk_file, 'r', encoding='utf-8') as f:
                    chunk_content = f.read()
                
                # Find the section description for this chunk
                section_desc = "Unknown Section"
                for section_id, details in directory.items():
                    if details["chunk_file"] == chunk_file:
                        section_desc = details["description"]
                        break
                
                # Add section header and content
                combined_chunks += f"\n--- REFERENCE SECTION {i}: {section_desc} ---\n"
                combined_chunks += chunk_content + "\n"
                
            except FileNotFoundError:
                combined_chunks += f"\n--- ERROR: Could not load {chunk_file} ---\n"
        
        # Create the prompt with combined chunks
        system_prompt = create_multi_agent_r_prompt(combined_chunks, sub_query)
        
        # Initialize Agent R_i client
        agent_r = initialize_openrouter_client(AGENT_R_MODEL)
        
        # Get response
        messages = [SystemMessage(content=system_prompt)]
        response = agent_r.invoke(messages)
        
        return response.content.strip()
        
    except Exception as e:
        return f"Error querying Agent R_i with multiple chunks: {e}"

# Legacy function for backward compatibility
def query_agent_r(chunk_file: str, sub_query: str) -> str:
    """Legacy function - delegates to single chunk query."""
    return query_agent_r_single(chunk_file, sub_query)

# =============================================================================
# RESPONSE SYNTHESIS
# =============================================================================

def synthesize_response(original_query: str, agent_r_response: str) -> str:
    """
    Have Agent A synthesize the final response from Agent R_i's output.
    
    Args:
        original_query: The user's original question
        agent_r_response: Agent R_i's factual response
        
    Returns:
        Agent A's synthesized, conversational response
    """
    synthesis_prompt = f"""You are Agent A. You delegated a user's question to a reference agent and received a factual response. Now synthesize this information into a natural, conversational answer that directly addresses the user's original query.

Original user query: "{original_query}"

Reference agent's response: "{agent_r_response}"

Please rephrase this information into a natural, conversational answer that directly addresses the user's question. Make it sound helpful and engaging, not robotic."""

    try:
        # Initialize Agent A client for synthesis
        agent_a = initialize_openrouter_client(AGENT_A_MODEL)
        
        # Get synthesized response
        messages = [SystemMessage(content=synthesis_prompt)]
        response = agent_a.invoke(messages)
        
        return response.content.strip()
        
    except Exception as e:
        print(f"Error during synthesis: {e}")
        return agent_r_response  # Fallback to raw Agent R_i response

# =============================================================================
# MAIN SYSTEM WORKFLOW
# =============================================================================

def process_user_query(user_query: str, directory: Dict) -> str:
    """
    Process a user query through the two-layer system.
    
    Args:
        user_query: The user's question
        directory: The knowledge directory
        
    Returns:
        The final response to the user
    """
    print(f"\n🤔 Processing query: {user_query}")
    
    # Step 1: Query Agent A for decision
    print("📋 Agent A is evaluating the query...")
    agent_a_decision = query_agent_a(user_query, directory)
    
    # Handle errors
    if "error" in agent_a_decision:
        return "I encountered an error processing your query. Please try rephrasing it."
    
    # Step 2: Process based on Agent A's decision
    if not agent_a_decision.get("needs_reference", False):
        # Agent A can answer directly
        print("✅ Agent A is answering directly")
        return agent_a_decision.get("answer", "I couldn't generate a proper response.")
    
    else:
        # Agent A wants to delegate
        scope = agent_a_decision.get("scope")
        sub_query = agent_a_decision.get("sub_query")
        reason = agent_a_decision.get("reason", "")
        
        # Handle both single scope (backward compatibility) and multiple scopes
        if isinstance(scope, str):
            # Single scope (legacy format)
            scope_list = [scope]
        elif isinstance(scope, list):
            # Multiple scopes (new format)
            scope_list = scope
        else:
            return "I encountered an error with the scope format. Please try rephrasing your query."
        
        print(f"🔍 Agent A is delegating to {len(scope_list)} reference section(s): {scope_list}")
        print(f"📝 Reason: {reason}")
        
        # Validate that all requested scopes exist
        missing_scopes = [s for s in scope_list if s not in directory]
        if missing_scopes:
            return f"I wanted to check my reference material for {missing_scopes}, but those sections don't exist in my knowledge base."
        
        # Step 3: Query Agent R_i with single or multiple chunks
        if len(scope_list) == 1:
            # Single chunk query
            chunk_file = directory[scope_list[0]]["chunk_file"]
            section_desc = directory[scope_list[0]]["description"]
            print(f"📚 Querying Agent R_i with section: {section_desc}")
            
            agent_r_response = query_agent_r_single(chunk_file, sub_query)
            
        else:
            # Multiple chunk query
            chunk_files = [directory[s]["chunk_file"] for s in scope_list]
            section_descs = [directory[s]["description"] for s in scope_list]
            print(f"📚 Querying Agent R_i with {len(chunk_files)} sections:")
            for desc in section_descs:
                print(f"   • {desc}")
            
            agent_r_response = query_agent_r_multiple(chunk_files, sub_query, directory)
        
        # Step 4: Synthesize final response
        print("🔄 Agent A is synthesizing the final response...")
        final_response = synthesize_response(user_query, agent_r_response)
        
        return final_response

def main():
    """Main application loop."""
    print("=" * 60)
    print("Two-Layer Agentic Knowledge System")
    print("=" * 60)
    print("Commands:")
    print("  load <filename.md>  - Load a markdown document")
    print("  help               - Show this help")
    print("  quit               - Exit the system")
    print("  <question>         - Ask a question")
    print()
    
    # Ensure directories exist
    ensure_directories()
    
    # Load existing directory
    directory = load_directory()
    print(f"📁 Loaded knowledge base with {len(directory)} sections")
    
    # Check API key
    global OPENROUTER_API_KEY
    if OPENROUTER_API_KEY == "YOUR_OPENROUTER_API_KEY_HERE":
        print("\n⚠️  WARNING: Please set your OpenRouter API key in the script!")
        print("   Edit the OPENROUTER_API_KEY variable at the top of this script.")
        api_key = input("\nEnter your OpenRouter API key now (or press Enter to continue with placeholder): ").strip()
        if api_key:
            OPENROUTER_API_KEY = api_key
        else:
            print("   You can continue testing the system, but API calls will fail.")
    
    print("\n💬 Ready! Ask me anything or use 'load <filename.md>' to add knowledge.")
    
    # Main interaction loop
    while True:
        try:
            user_input = input("\n> ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            elif user_input.lower() == 'help':
                print("\nCommands:")
                print("  load <filename.md>  - Load a markdown document")
                print("  help               - Show this help")
                print("  quit               - Exit the system")
                print("  <question>         - Ask a question")
                
            elif user_input.lower().startswith('load '):
                filename = user_input[5:].strip()
                if load_document(filename):
                    directory = load_directory()  # Reload directory
                    print(f"📁 Knowledge base now has {len(directory)} sections")
                
            else:
                # Process as a query
                if len(directory) == 0:
                    print("📝 No knowledge base loaded yet. Use 'load <filename.md>' to add documents first.")
                else:
                    response = process_user_query(user_input, directory)
                    print(f"\n💡 {response}")
                    
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
