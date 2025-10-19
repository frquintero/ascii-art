This is the structure of prompts in @.github/prompts

.github/prompts/
├── speckit.analyze.prompt.md
├── speckit.checklist.prompt.md
├── speckit.clarify.prompt.md
├── speckit.constitution.prompt.md
├── speckit.implement.prompt.md
├── speckit.plan.prompt.md
├── speckit.specify.prompt.md
└── speckit.tasks.prompt.md

Each prompt file contains instructions for a specific agent role in the Speckit system. The prompts guide the agents on how to process user input, update project documentation, and ensure consistency across related artifacts. Each prompt follows a structured format, outlining the steps the agent must take to complete its task effectively.

The prompts are designed to be used in conjunction with the agents in the Speckit system. Each agent has its own subdirectory under @.specify/, and when the user runs /command (v.g. /constitution) the agent will run the corresponding prompt file (v.g. speckit.constitution.prompt.md) from the @.github/prompts/ directory. The prompt file will provide the agent with the necessary instructions and guidance to complete its task effectively.

Do not modify this file directly.
