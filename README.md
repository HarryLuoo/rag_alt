# Two-Layer Agentic Knowledge System

A prototype implementation of a two-layer agentic system that demonstrates an alternative to traditional RAG (Retrieval-Augmented Generation) approaches. The system uses direct knowledge chunk injection rather than semantic similarity matching.

## 🏗️ Architecture Overview

### **Layer 1: Agent A (Frontend Gatekeeper)**
- **Role**: Lightweight decision-maker and query router
- **Model**: `google/gemma-3n-e2b-it:free` (via OpenRouter)
- **Function**: 
  - Evaluates user queries with confidence scoring (1-10)
  - Answers directly if confidence ≥ 8
  - Delegates to Layer 2 if confidence < 8
  - Synthesizes final responses from Agent R_i outputs

### **Layer 2: Agent R_i (Reference Agents)**
- **Role**: Specialized knowledge processors
- **Model**: `google/gemma-3-12b-it:free` (via OpenRouter)  
- **Function**:
  - Dynamically instantiated per request
  - Receives specific knowledge chunks directly
  - Answers based ONLY on provided text content
  - No external knowledge contamination

### **Knowledge Directory**
- **Structure**: JSON index mapping sections to chunk files
- **Purpose**: Enables Agent A awareness without loading full content
- **Format**: Lean summaries with `section_id` and `description` only

## 📁 Project Structure

```
rag_alt/
├── two_layer_agentic_system.py    # Main system implementation
├── build_knowledge.py             # Knowledge parsing and directory builder
├── demo_system.py                 # Demo without API key required
├── requirements.txt               # Python dependencies
├── directory.json                 # Knowledge index (auto-generated)
├── chunks/                        # Individual knowledge chunks (auto-generated)
│   ├── teleportation_manual_section_1.txt
│   ├── teleportation_manual_section_2.txt
│   ├── [...other chunks...]
│   └── planet_kepler_vorthak_section_5.txt
├── teleportation_manual.md        # Source: Fictional teleportation device manual
├── planet_kepler_vorthak.md       # Source: Fictional planet documentation
└── README.md                      # This file
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Build Knowledge Base
```bash
python build_knowledge.py
```
This processes the markdown files and creates:
- `directory.json` - Knowledge index
- `chunks/` directory with individual section files

### 3. Run Demo (No API Key Required)
```bash
python demo_system.py
```
Experience the system logic with simulated responses.

### 4. Configure API Key
Create your configuration file:
```bash
cp config.py.example config.py
```
Edit `config.py` and replace `YOUR_OPENROUTER_API_KEY_HERE` with your actual OpenRouter API key.

### 5. Run Full System (Requires OpenRouter API Key)
```bash
python two_layer_agentic_system.py
```

## 🔑 API Key Setup

You need an [OpenRouter](https://openrouter.ai) API key to run the full system:

1. Sign up at https://openrouter.ai
2. Copy `config.py.example` to `config.py`
3. Edit `config.py` and add your API key
4. The `config.py` file is gitignored to keep your key secure
2. Get your API key from the dashboard
3. Either:
   - Edit `OPENROUTER_API_KEY` in `two_layer_agentic_system.py`, or
   - Enter it when prompted during runtime

## 📚 Knowledge Base

The system currently contains two fictional knowledge domains:

### **QuantumPort X7-Delta Teleportation Device**
- **Sections**: 4 chunks covering specifications, operations, troubleshooting, and advanced settings
- **Content**: Detailed technical manual with specific measurements, procedures, and error codes
- **Purpose**: Demonstrates technical documentation processing

### **Planet Kepler-Vorthak**
- **Sections**: 5 chunks covering planetary characteristics, atmosphere, geology, life forms, and resources
- **Content**: Comprehensive planetary survey with unique scientific details
- **Purpose**: Demonstrates scientific documentation processing

## 🎯 Key Features

### **Direct Knowledge Injection**
- No vector embeddings or semantic search
- Agent R_i receives complete, relevant text chunks
- Eliminates context matching ambiguity

### **Self-Aware Decision Making**
- Agent A uses confidence scoring for delegation decisions
- Transparent reasoning with structured JSON responses
- Fallback mechanisms for edge cases

### **Dynamic Agent Instantiation**
- Agent R_i created on-demand per query
- Each instance can process single or multiple knowledge chunks
- Scalable to unlimited knowledge domains
- Multi-source reasoning for complex queries

### **Response Synthesis**
- Agent A transforms technical responses into conversational answers
- Maintains accuracy while improving user experience
- No generic template responses

## 🔄 System Workflow

```mermaid
graph TD
    A[User Query] --> B[Agent A: Evaluate Query]
    B --> C{Confidence ≥ 8?}
    C -->|Yes| D[Agent A: Direct Answer]
    C -->|No| E[Agent A: Select Knowledge Section(s)]
    E --> F{Single or Multiple Sections?}
    F -->|Single| G[Agent R_i: Process One Chunk]
    F -->|Multiple| H[Agent R_i: Process Multiple Chunks]
    G --> I[Agent A: Synthesize Response]
    H --> I
    D --> J[Final Response to User]
    I --> J
```

## 🧠 Multi-Source Reasoning

The system now supports **multi-chunk queries** where Agent A can select multiple relevant knowledge sections for complex questions:

**Single-Source Query:**
- User: "What are the teleportation device specifications?"
- Agent A: Selects `teleportation_manual_chapter_1`
- Agent R_i: Processes one chunk with device specs

**Multi-Source Query:**
- User: "Compare the teleportation device energy requirements with the planet's energy resources"
- Agent A: Selects `["teleportation_manual_chapter_1", "planet_kepler_vorthak_chapter_3"]`
- Agent R_i: Processes both chunks together and synthesizes comparison

This enables comprehensive answers that draw from multiple knowledge domains simultaneously.

## 🧪 Example Queries

Try asking questions like:

**Teleportation Device:**
- "What are the specifications of the QuantumPort X7-Delta?"
- "How do I safely operate the teleportation device?"
- "What should I do if I get error code QP-4401?"
- "What are the advanced configuration options?"

**Planet Kepler-Vorthak:**
- "What's the atmosphere like on Kepler-Vorthak?"
- "What kind of life exists on the planet?"
- "Describe the geological features of the planet"
- "What resources can be mined from Kepler-Vorthak?"

## 🔧 Adding New Knowledge

### Method 1: Markdown Files
1. Create a new `.md` file with H2 section headings (`## Section Title`)
2. Run `python build_knowledge.py` to update the system
3. The system automatically processes new sections

### Method 2: Runtime Loading
1. Run the main system: `python two_layer_agentic_system.py`
2. Use the `load <filename.md>` command
3. Knowledge is immediately available for queries

## 🛠️ Configuration

### Models
- **Agent A**: Lightweight model for decision-making
- **Agent R_i**: More capable model for knowledge processing
- Both configurable in `two_layer_agentic_system.py`

### File Paths
- `DIRECTORY_FILE`: Knowledge index location
- `CHUNKS_DIR`: Individual chunk storage directory

### API Settings
- `OPENROUTER_BASE_URL`: OpenRouter API endpoint
- Models use OpenRouter's free tier by default

## 🎭 Demo Mode Features

The `demo_system.py` provides:
- Full system logic simulation
- No API key required
- Rule-based response generation
- Perfect for testing and demonstration

## 🚨 Error Handling

The system includes robust error handling for:
- Malformed JSON responses from Agent A
- Missing knowledge chunks
- API connectivity issues
- File I/O operations
- Graceful degradation when components fail

## 🔍 Advantages Over Traditional RAG

1. **No Semantic Matching Issues**: Direct chunk access eliminates retrieval ambiguity
2. **Transparent Knowledge Routing**: Clear decision logic for Agent A
3. **Isolated Agent Processing**: Each Agent R_i works with complete, relevant context
4. **Iterative Query Support**: Can spawn multiple Agent R_i for complex queries
5. **Deterministic Behavior**: Predictable routing based on directory structure

## 📈 Future Enhancements

- **Multi-chunk queries**: Allow Agent R_i to access multiple related sections
- **Knowledge versioning**: Track changes to knowledge base over time
- **Custom models**: Support for different model providers beyond OpenRouter
- **Batch processing**: Handle multiple queries simultaneously
- **Knowledge validation**: Automated fact-checking across chunks

## 🤝 Contributing

This is a prototype implementation demonstrating the two-layer agentic approach. Feel free to:
- Experiment with different models
- Add new knowledge domains
- Improve the decision logic
- Enhance error handling
- Optimize performance

## 📄 License

This project is provided as-is for educational and research purposes. The fictional knowledge content (teleportation device and planet descriptions) is original creative content included for demonstration.

---

**Built with Python, LangChain, and OpenRouter API**
