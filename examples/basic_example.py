from flightdeck import App, BaseAgent
from flightdeck.utils import find_plugins, select_plugin, fill_slots

app = App()

@find_plugins
@select_plugin
@fill_slots
class Agent(BaseAgent):
    async def preprocess(self):
        pass

    async def postprocess(self):
        pass


app.add_agent(Agent)


@app.route("/whitespace")
async def whitespace(agent: Agent)
  with agent as a:
      whitespace_safe_messages = []
      for message in a.context.messages:
          whitespace_safe_messages.append(message.strip())
      a.context.messages = whitespace_safe_messages
      a.invoke()


@app.route("/workflow")
async def workflow(context: CopilotContext):
    with Agent.create(context) as agent:
        plugins = agent.find_plugins(n=10)
        plugin = agent.select_plugin(plugins)
        plugin = agent.slot_fill_plugin(plugin)
        result = plugin.invoke()
        return result

if __name__ == "__main__":
    app.serve()
