# FlightDeck

FlightDeck is a Python SDK that helps developers create and run AI copilot agents. It provides a simple and intuitive API to build, train, and deploy AI copilot agents.

## Installation

You can install FlightDeck using pip:

```bash
pip install flightdeck
```

## Usage

Here's a basic example of how to use FlightDeck:

```python
from flightdeck import App
from flightdeck.agents import PluginAgent

# Initialize the app
app = App()

# register the agent with a function
@app.agent(PluginAgent)
@app.get("/conversation/{uuid}")
def chat(uuid):
    agent = app.agent
    return agent.conversation(uuid)

# or let flightdeck handle it with dependency injection
@app.post("/conversation/{uuid}")
def chat(uuid: str, agent: PluginAgent, request_payload: dict):
    agent.update_conversation(uuid, request_payload)
    agent()
    return agent.conversation(uuid)

if __name__ == "__main__":
    # serve the copilot app
    app.serve()
```

For more detailed usage examples, please check the `examples/` directory.

## Documentation

The complete documentation for FlightDeck is available on [Read the Docs](https://flightdeck.readthedocs.io).

## Testing

To run the tests, use the following command:

```bash
python -m unittest discover tests
```

## Contributing

We welcome contributions! Please see our [contributing guide](CONTRIBUTING.md) for more details.

## License

FlightDeck is licensed under the [MIT License](LICENSE).