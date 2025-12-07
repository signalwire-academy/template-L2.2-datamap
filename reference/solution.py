#!/usr/bin/env python3
"""DataMap integration agent.

Lab 2.2 Deliverable: Demonstrates DataMap configuration for external
API calls with GET, POST, and error handling patterns.
"""

from signalwire_agents import AgentBase
from signalwire_agents.core.data_map import DataMap
from signalwire_agents.core.function_result import SwaigFunctionResult


class DataMapAgent(AgentBase):
    """Agent with DataMap integrations for external APIs."""

    def __init__(self):
        super().__init__(name="datamap-agent")

        self.prompt_add_section(
            "Role",
            "You help look up user and post information from our database."
        )

        self.prompt_add_section(
            "Capabilities",
            bullets=[
                "Look up user information by ID",
                "Create new blog posts",
                "Retrieve existing posts"
            ]
        )

        self.add_language("English", "en-US", "rime.spore")
        self._setup_datamaps()

    def _setup_datamaps(self):
        """Configure DataMaps for external API calls."""

        # GET request - User lookup
        get_user_dm = (
            DataMap("get_user")
            .description("Look up user information by ID")
            .parameter("user_id", "string", "The user ID (1-10)", required=True)
            .webhook(
                "GET",
                "https://jsonplaceholder.typicode.com/users/${args.user_id}"
            )
            .output(SwaigFunctionResult(
                "User ${name} has email ${email}"
            ))
            .fallback_output(SwaigFunctionResult(
                "Could not find user with that ID."
            ))
        )
        self.register_swaig_function(get_user_dm.to_swaig_function())

        # POST request - Create post
        create_post_dm = (
            DataMap("create_post")
            .description("Create a new blog post")
            .parameter("title", "string", "Post title", required=True)
            .parameter("body", "string", "Post content", required=True)
            .webhook(
                "POST",
                "https://jsonplaceholder.typicode.com/posts"
            )
            .body({
                "title": "${args.title}",
                "body": "${args.body}",
                "userId": 1
            })
            .output(SwaigFunctionResult(
                "Post created with ID ${id}. Title: ${title}"
            ))
            .fallback_output(SwaigFunctionResult(
                "Failed to create the post."
            ))
        )
        self.register_swaig_function(create_post_dm.to_swaig_function())

        # GET request with error handling
        get_post_dm = (
            DataMap("get_post")
            .description("Get a blog post by ID")
            .parameter("post_id", "string", "The post ID", required=True)
            .webhook(
                "GET",
                "https://jsonplaceholder.typicode.com/posts/${args.post_id}"
            )
            .output(SwaigFunctionResult(
                "Post ${id}: ${title}"
            ))
            .fallback_output(SwaigFunctionResult(
                "I couldn't find a post with that ID. Please try another."
            ))
        )
        self.register_swaig_function(get_post_dm.to_swaig_function())

        # Challenge: Get posts by user
        get_user_posts_dm = (
            DataMap("get_user_posts")
            .description("Get all posts by a specific user")
            .parameter("user_id", "string", "The user ID", required=True)
            .webhook(
                "GET",
                "https://jsonplaceholder.typicode.com/posts?userId=${args.user_id}"
            )
            .output(SwaigFunctionResult(
                "Found posts for user ${args.user_id}."
            ))
            .fallback_output(SwaigFunctionResult(
                "Could not retrieve posts for that user."
            ))
        )
        self.register_swaig_function(get_user_posts_dm.to_swaig_function())


if __name__ == "__main__":
    agent = DataMapAgent()
    agent.run()
