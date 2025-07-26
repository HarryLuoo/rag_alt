#!/usr/bin/env python3
"""
Two-Layer Agentic System Demo (Without API)
===========================================

This demo shows how the system would work by simulating the Agent decisions
without actually calling the OpenRouter API. This lets you test the logic
and see the flow without needing an API key.
"""

import json
import re
from pathlib import Path

# Import functions from the main script
from two_layer_agentic_system import (
    load_directory, 
    create_directory_summary,
    create_agent_a_prompt,
    create_agent_r_prompt
)

def simulate_agent_a_decision(user_query: str, directory: dict) -> dict:
    """
    Simulate Agent A's decision-making process based on query analysis.
    This replaces the actual API call with rule-based logic for demo purposes.
    """
    user_query_lower = user_query.lower()
    
    # Keywords that suggest teleportation device questions
    teleport_keywords = [
        'teleport', 'quantum', 'device', 'x7-delta', 'quantumport', 
        'specifications', 'components', 'operating', 'safety', 'troubleshooting',
        'malfunction', 'configuration', 'zeridium', 'heisenberg', 'cooldown'
    ]
    
    # Keywords that suggest planet questions
    planet_keywords = [
        'planet', 'kepler', 'vorthak', 'orbital', 'atmosphere', 'weather',
        'geological', 'terrain', 'flora', 'fauna', 'resources', 'mining',
        'gravity', 'binary', 'star', 'xenophine'
    ]
    
    # Check if query matches teleportation device content
    teleport_matches = sum(1 for keyword in teleport_keywords if keyword in user_query_lower)
    planet_matches = sum(1 for keyword in planet_keywords if keyword in user_query_lower)
    
    if teleport_matches > 0:
        # Find the most relevant teleportation section
        if any(word in user_query_lower for word in ['spec', 'component', 'size', 'weight']):
            scope = "teleportation_manual_section_1"
        elif any(word in user_query_lower for word in ['operate', 'use', 'safety', 'procedure']):
            scope = "teleportation_manual_section_2"
        elif any(word in user_query_lower for word in ['problem', 'error', 'troubleshoot', 'fix']):
            scope = "teleportation_manual_section_3"
        elif any(word in user_query_lower for word in ['advanced', 'config', 'setting', 'precision']):
            scope = "teleportation_manual_section_4"
        else:
            scope = "teleportation_manual_section_1"  # Default to specs
            
        return {
            "needs_reference": True,
            "scope": scope,
            "sub_query": f"Please answer this question about the teleportation device: {user_query}",
            "reason": "This question requires specific technical information about the teleportation device."
        }
    
    elif planet_matches > 0:
        # Find the most relevant planet section
        if any(word in user_query_lower for word in ['orbit', 'size', 'gravity', 'characteristic']):
            scope = "planet_kepler_vorthak_section_1"
        elif any(word in user_query_lower for word in ['atmosphere', 'weather', 'air', 'gas']):
            scope = "planet_kepler_vorthak_section_2"
        elif any(word in user_query_lower for word in ['terrain', 'geological', 'canyon', 'desert', 'floating']):
            scope = "planet_kepler_vorthak_section_3"
        elif any(word in user_query_lower for word in ['life', 'flora', 'fauna', 'animals', 'plants']):
            scope = "planet_kepler_vorthak_section_4"
        elif any(word in user_query_lower for word in ['resource', 'mining', 'mineral', 'crystal']):
            scope = "planet_kepler_vorthak_section_5"
        else:
            scope = "planet_kepler_vorthak_section_1"  # Default to characteristics
            
        return {
            "needs_reference": True,
            "scope": scope,
            "sub_query": f"Please answer this question about planet Kepler-Vorthak: {user_query}",
            "reason": "This question requires specific information about planet Kepler-Vorthak."
        }
    
    else:
        # General questions that Agent A might answer directly
        general_questions = [
            'hello', 'hi', 'what can you do', 'help', 'how are you',
            'what is your name', 'who are you'
        ]
        
        if any(phrase in user_query_lower for phrase in general_questions):
            return {
                "needs_reference": False,
                "answer": "Hello! I'm an AI assistant with access to specialized knowledge about a teleportation device (QuantumPort X7-Delta) and a fictional planet (Kepler-Vorthak). I can answer questions about their technical specifications, operations, and characteristics. What would you like to know?"
            }
        else:
            return {
                "needs_reference": False,
                "answer": "I'm not sure I have specific information about that topic. I have detailed knowledge about the QuantumPort X7-Delta teleportation device and planet Kepler-Vorthak. Could you ask me something about those topics instead?"
            }

def simulate_agent_r_response(chunk_file: str, sub_query: str) -> str:
    """
    Simulate Agent R_i by reading the chunk and providing a relevant excerpt.
    In the real system, this would be handled by the AI model.
    """
    try:
        with open(chunk_file, 'r', encoding='utf-8') as f:
            chunk_content = f.read()
        
        # Extract the first few paragraphs as a simulated response
        paragraphs = chunk_content.split('\n\n')
        
        # Take up to 3 paragraphs for a reasonable response length
        response_content = '\n\n'.join(paragraphs[:3])
        
        return f"Based on the technical documentation, here's the relevant information:\n\n{response_content}"
        
    except FileNotFoundError:
        return f"Error: Could not access the reference material for this query."
    except Exception as e:
        return f"Error processing the reference material: {e}"

def demo_system():
    """Run a demo of the two-layer agentic system."""
    print("=" * 60)
    print("Two-Layer Agentic System DEMO")
    print("(Simulated - No API Key Required)")
    print("=" * 60)
    
    # Load the knowledge directory
    directory = load_directory()
    
    if not directory:
        print("❌ No knowledge directory found. Please run build_knowledge.py first.")
        return
    
    print(f"📁 Loaded knowledge base with {len(directory)} sections")
    print("\n🤖 Available knowledge topics:")
    print("   📡 QuantumPort X7-Delta Teleportation Device")
    print("   🪐 Planet Kepler-Vorthak")
    
    print("\n💡 Try asking questions like:")
    print("   • What are the specifications of the teleportation device?")
    print("   • How do I operate the X7-Delta safely?")
    print("   • What's the atmosphere like on Kepler-Vorthak?")
    print("   • What kind of life exists on the planet?")
    print("   • What troubleshooting steps should I follow?")
    
    print("\n💬 Demo Mode - Ask me anything! (Type 'quit' to exit)")
    
    while True:
        try:
            user_input = input("\n> ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Demo completed!")
                break
            
            print(f"\n🤔 Processing: {user_input}")
            
            # Step 1: Simulate Agent A decision
            print("📋 Agent A is evaluating the query...")
            agent_a_decision = simulate_agent_a_decision(user_input, directory)
            
            # Step 2: Process based on decision
            if not agent_a_decision.get("needs_reference", False):
                # Agent A answers directly
                print("✅ Agent A is answering directly")
                response = agent_a_decision.get("answer", "I couldn't generate a proper response.")
                print(f"\n💡 {response}")
                
            else:
                # Agent A delegates
                scope = agent_a_decision.get("scope")
                sub_query = agent_a_decision.get("sub_query")
                reason = agent_a_decision.get("reason", "")
                
                print(f"🔍 Agent A is delegating to: {scope}")
                print(f"📝 Reason: {reason}")
                
                if scope in directory:
                    chunk_file = directory[scope]["chunk_file"]
                    section_desc = directory[scope]["description"]
                    
                    print(f"📚 Consulting section: {section_desc}")
                    
                    # Step 3: Simulate Agent R_i
                    agent_r_response = simulate_agent_r_response(chunk_file, sub_query)
                    
                    # Step 4: Display the response (synthesis simulation)
                    print("🔄 Agent A is synthesizing the final response...")
                    print(f"\n💡 {agent_r_response}")
                    
                else:
                    print(f"\n❌ Error: Section '{scope}' not found in knowledge base.")
                
        except KeyboardInterrupt:
            print("\n👋 Demo completed!")
            break
        except Exception as e:
            print(f"❌ Demo error: {e}")

if __name__ == "__main__":
    demo_system()
