from flightdeck.agents import BaseAgent
from flightdeck.core import App
from flightdeck.core.workflows import task


class BaseAgent():
    def __init__(self, context, steps):
        self.context = context
        self.steps = steps
        self.history = {}

    def __call__(self):
        for step in self.steps:
            if self.history.get(step):
                continue
            step()
            self.validate()


class MyCopilotAgent(BaseAgent):

    @classmethod
    def create(context):
        plugin_search = PluginSearch.create(context)
        plugin_select = PluginSelect.create(context)
        slot_filler = SlotFiller.create(context)
        plugin_executor = PluginExecutor.create(context)
        responder = Responder.create(context)

        return MyCopilotAgent(
            context=context,
            steps=[
                plugin_search(input=None),
                plugin_select(input=plugin_search.output),
                slot_filler(input=plugin_select.output),
                plugin_executor(input=slot_filler.output),
                responder(input=plugin_executor.output)
            ]

@task
class PluginSelect():
    def __init__(self, context):
        self.context = context
        self._output = None
        self._inputs = None

    def output(self):
        return self._output

    def invoke(self):
        plugins = self._inputs()
        self._output = classify_intent(plugins)

    def __call__(self):
        return self.invoke

app = App()

@app.agent(MyCopilotAgent)
@app.POST("/conversations/{uuid}")
async def create(uuid: str, context: ConversationContext):
    conversation = ConversationService.get(uuid)
    copilot = app.get_agent(conversation)
    copilot.context.update(context)
    copilot()
    return copilot.conversation

if __name__ == "__main__":
    app.serve()
