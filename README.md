# Ollama Python Integration Examples

This repository contains practical Python scripts showcasing different approaches to integrate with Ollama for AI-powered applications.

## Setup Instructions

### 1. Install Ollama
Download and install Ollama for your operating system:
- **macOS**: `brew install ollama`
- **Linux**: `curl -fsSL https://ollama.ai/install.sh | sh`
- **Windows**: Download from [ollama.ai](https://ollama.ai/download)

### 2. Install Python Requirements
```bash
pip install requests ollama
```

### 3. Setup Model
```bash
# Pull the required model
ollama pull llama3.2

# Start Ollama service
ollama serve
```

## Script Documentation

### `1-send-prompt.py` - Raw HTTP API Implementation
Direct REST API interaction using the `requests` library. This approach gives you full control over the HTTP requests and is useful for understanding the underlying API structure.

**Key Features:**
- Manual HTTP request construction
- JSON response parsing
- Error handling with status codes
- Stream processing demonstration

### `2-generate.py` - Simple Text Generation
Minimal implementation using the official Ollama Python library. Perfect for basic text generation tasks.

**Key Features:**
- Streamlined API usage
- Real-time streaming output
- Clean, readable code structure

### `3-chat.py` - Basic Conversation Interface
Implements structured conversation format with role-based messaging system.

**Key Features:**
- Message-based conversation structure
- Single-turn interactions
- Complete response handling

### `4-stream-chat.py` - Real-time Chat Streaming
Enhanced version of the chat interface with streaming capabilities for better user experience.

**Key Features:**
- Live response streaming
- Improved perceived performance
- Real-time output display

### `5-chat-with-user.py` - Interactive Chat System
Full-featured conversational AI with persistent memory and customizable parameters.

**Key Features:**
- Continuous conversation loop
- Conversation history management
- Configurable AI personality via system prompts
- Advanced parameter tuning:
  - Temperature control for creativity
  - Token limiting with top_k and top_p
  - Response streaming for real-time interaction

### `6-with-model-create.py` - Custom Model Management
Demonstrates model creation, configuration, and lifecycle management.

**Key Features:**
- Dynamic model creation from base models
- Comprehensive parameter configuration
- System prompt customization
- Automatic model cleanup
- Advanced generation parameters:
  - Repetition penalties
  - Context window sizing
  - Token prediction limits
  - Custom stop sequences
  - Seed-based reproducibility

## Configuration Parameters Reference

### Core Parameters
| Parameter | Range | Description | Default |
|-----------|-------|-------------|---------|
| `temperature` | 0.0-2.0 | Response creativity level | 0.7 |
| `top_p` | 0.0-1.0 | Nucleus sampling threshold | 0.9 |
| `top_k` | 1-100 | Token candidate limitation | 50 |
| `repeat_penalty` | >1.0 | Repetition avoidance | 1.1 |
| `num_ctx` | 512-32768 | Context window size | 4096 |
| `num_predict` | 1-2048 | Maximum response tokens | 256 |

### Advanced Parameters
- **presence_penalty**: Encourages topic diversity (-2.0 to 2.0)
- **frequency_penalty**: Reduces token repetition based on frequency (-2.0 to 2.0)
- **stop**: Custom sequences to halt generation
- **seed**: Ensures reproducible outputs

## Usage Patterns

### Quick Text Generation
Use scripts 1-2 for simple, one-off text generation tasks.

### Conversational Applications
Scripts 3-5 provide escalating levels of conversation complexity, from basic Q&A to full interactive sessions.

### Production Integration
Script 6 demonstrates production-ready patterns including model lifecycle management and parameter optimization.

## Development Workflow

1. **Start with Script 2**: Understand basic generation
2. **Explore Script 3**: Learn conversation structure
3. **Add Streaming (Script 4)**: Improve user experience
4. **Implement History (Script 5)**: Build context awareness
5. **Customize Models (Script 6)**: Fine-tune for specific use cases

## Error Handling

### Common Issues
- **Connection Errors**: Ensure Ollama server is running (`ollama serve`)
- **Model Not Found**: Download required models (`ollama pull <model-name>`)
- **Import Errors**: Install dependencies (`pip install requests ollama`)
- **Port Conflicts**: Use `OLLAMA_HOST` environment variable for custom ports

### Best Practices
- Always check response status codes
- Implement proper exception handling
- Validate model availability before use
- Monitor resource usage for large models

## Performance Considerations

### Memory Usage
- Smaller models (7B): ~4-6GB RAM
- Medium models (13B): ~8-12GB RAM
- Large models (70B+): 40GB+ RAM or multiple GPUs

### Response Speed
- Streaming responses improve perceived performance
- Model size directly impacts generation speed
- GPU acceleration significantly improves performance

## Extending the Examples

### Adding New Features
- Image processing with LLaVA models
- Document analysis and summarization
- Multi-model orchestration
- Custom fine-tuning workflows

### Integration Ideas
- Web API development with Flask/FastAPI
- Discord/Slack bot implementations
- CLI tool creation
- Desktop application integration

## Additional Resources

- [Ollama Official Documentation](https://github.com/ollama/ollama)
- [Ollama Python Library](https://github.com/ollama/ollama-python)
- [Model Library](https://ollama.ai/library)
- [API Reference](https://github.com/ollama/ollama/blob/main/docs/api.md)

## File Structure
```
project/
├── 1-send-prompt.py
├── 2-generate.py
├── 3-chat.py
├── 4-stream-chat.py
├── 5-chat-with-user.py
├── 6-with-model-create.py
└── README.md
```