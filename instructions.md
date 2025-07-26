

# Instructions for Building the Two-Layer Agentic System Prototype

Hello Cline,

Your task is to generate a complete, self-contained Python script that implements the two-layer agentic knowledge system described below. The prototype will use **Python**, **LangChain**, and the **OpenRouter API**.

Please adhere strictly to the design document provided. Pay close attention to the **Key Implementation Directives** listed below, as they contain critical clarifications to guide your implementation.

## Key Implementation Directives

Before you begin writing the code, review these essential rules:

1.  **Directory Summary for Agent A's Prompt:** The "directory summary" passed into Agent A's prompt must be a lean JSON string. It should **only** contain the `section_id` and `description` for each entry. Do not include file paths or other metadata in the prompt context, as this is designed to keep Agent A's context window efficient.

2.  **Knowledge Parsing Logic:** The knowledge parsing function must be implemented to handle simple Markdown (`.md`) files. Assume that each new knowledge chunk is separated by a Markdown H2 heading (e.g., `## Clause 1: Introduction`). The text of the heading itself should be used as the `description` for that chunk in the directory.

3.  **Response Synthesis by Agent A:** When Agent A receives a factual response from an Agent R_i, it must perform a final synthesis step. The prompt for this step should instruct Agent A to rephrase Agent R_i's output into a natural, conversational answer that directly addresses the user's original query. **Do not** simply prepend static text like `"Agent A synthesis:"`.

4.  **OpenRouter Client Initialization:** When initializing the LangChain client for OpenRouter, use the `ChatOpenAI` class. You must configure it with the OpenRouter `openai_api_base` URL (`https://openrouter.ai/api/v1`) and the `openai_api_key`. Provide clear placeholders in the code for the user's OpenRouter API key.

5.  **Code Structure and Comments:** Please generate a single, self-contained Python script. Include comments to delineate major sections of the code, mapping them back to the components in the design document (e.g., `# --- Agent A Decision Logic ---`, `# --- Knowledge Base Parsing ---`).

---

## Full Design Document

### 1. System Overview and Goals

**Core Architecture**
- **Layer 1: Agent A** (Frontend Gatekeeper): A lightweight model that handles user queries, assesses its own knowledge limits, and decides when to delegate to Layer 2. It uses a directory for awareness of available knowledge chunks.
- **Layer 2: Agent R_i** (Reference Agents): Dynamically instantiated per request, each receiving a specific knowledge chunk and a tailored prompt. This enables direct, transparent access to full references.
- **Directory**: A lightweight index (e.g., JSON dict) mapping knowledge sections to chunk details. Updated on knowledge base changes.
- **Knowledge Base Handling**: Upon uploading a document, parse it into sections (e.g., clauses) and store chunks for retrieval. Each chunk is assigned to a potential Agent R_i entry in the directory.

**Key Ideas and Differentiators**
- **Decision-Making in Agent A**: Instill self-awareness via reflective prompting and confidence scoring (e.g., rate 1-10). Include a summary of the directory in Agent A's context to know when references are available. If confidence is low (<8), scope the query and delegate.
- **On-Demand Instantiation**: Agent R_i are not pre-loaded; create them dynamically by passing the relevant chunk to a model instance via OpenRouter. Prompts differentiate each R_i.
- **Advantages Over RAG**: Direct chunk injection avoids semantic matching issues; supports iterative/multi-response queries by spawning multiple R_i as needed.
- **Prototype Focus**: Build a simple Python script demonstrating the full workflow with OpenRouter. Use a free model for Agent A and a capable one for R_i (e.g., `deepseek/deepseek-r1-distill-llama-70b:free`).

### 2. Detailed Components

**Agent A**
- **Model**: Lightweight model via OpenRouter.
- **Context and Awareness**: Embed a directory summary in the system prompt. Use reflective logic to evaluate queries.
- **Decision Process**:
    1. Receive user query.
    2. Self-assess confidence (1-10) and check if reference is needed.
    3. If needed, scope the request (e.g., "clause_5") based on the directory.
    4. Output a structured JSON object: `{"needs_reference": bool, "scope": str, "sub_query": str, "reason": str}`.
- **Prompt Idea**:
    ```
    You are Agent A, a helpful but concise assistant with limited knowledge. Your available reference material is summarized in this directory: [INSERT JSON SUMMARY].

    For the user's query: "[USER QUERY]"

    First, determine if you can answer confidently on your own. Rate your confidence from 1 to 10.
    If your confidence is 8 or higher, answer directly.
    If your confidence is below 8, you must consult a reference. Identify the most relevant section from the directory to answer the query.

    Respond ONLY in JSON format.
    - If answering directly, use: {"needs_reference": false, "answer": "Your direct answer here."}
    - If delegating, use: {"needs_reference": true, "scope": "directory_section_id", "sub_query": "A precise question for the reference agent.", "reason": "Why you need the reference."}
    ```

**Directory**
- **Structure**: JSON file (`directory.json`), e.g.:
    ```json
    {
      "clause_1": {"description": "Clause 1: Introduction", "chunk_file": "chunks/clause_1.txt"},
      "clause_2": {"description": "Clause 2: Liability Terms", "chunk_file": "chunks/clause_2.txt"}
    }
    ```
- **Maintenance**: A function to parse an uploaded file, store chunks as text files (e.g., in a `chunks/` directory), and update the `directory.json` file.

**Agent R_i**
- **Instantiation**: Dynamically create a chat completion call using OpenRouter for each required reference.
- **Prompt Differentiation**: Use a specific prompt for each instance: `"You are a meticulous expert tasked with answering a question based ONLY on the following text. Do not use any outside knowledge. Text: [INSERT CHUNK TEXT]. Question: [INSERT SUB_QUERY]"`

### 3. Prototype Implementation Details

- **Main Workflow**:
    1. On script start, check for and load `directory.json`.
    2. Provide a function to parse a new document and populate the directory and `chunks/` folder.
    3. Create a main loop to accept user input.
    4. In the loop, call Agent A.
    5. If Agent A decides to delegate, fetch the relevant chunk text, call Agent R_i, and then pass the result back to Agent A for final synthesis.
    6. Print the final, synthesized response to the user.
- **Error Handling**: Include basic `try-except` blocks for API calls and file operations. If JSON output from Agent A is malformed, print an error and ask the user to rephrase.