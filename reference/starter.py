#!/usr/bin/env python3
"""Lab 2.2: DataMap Integration - Starter Template

Complete the TODOs to implement the lab requirements.
"""

from signalwire_agents import AgentBase
from signalwire_agents.core.data_map import DataMap
from signalwire_agents.core.function_result import SwaigFunctionResult


class DataMapAgent(AgentBase):
    def __init__(self):
        super().__init__(name="datamap-agent", route="/agent")

        self.prompt_add_section(
            "Role",
            "You help look up user and post information from our database."
        )

        self.add_language("English", "en-US", "rime.spore")

        # TODO: Add DataMap functions using the builder pattern
        # Example:
        # dm = (
        #     DataMap("function_name")
        #     .description("What this function does")
        #     .parameter("param", "string", "Description", required=True)
        #     .webhook("GET", "https://api.example.com/${args.param}")
        #     .output(SwaigFunctionResult("Response: ${field}"))
        #     .fallback_output(SwaigFunctionResult("Error message"))
        # )
        # self.register_swaig_function(dm.to_swaig_function())


agent = DataMapAgent()

if __name__ == "__main__":
    agent.run()
