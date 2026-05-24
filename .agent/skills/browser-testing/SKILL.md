---
description: Test the web application using a browser subagent to verify key functionality like adding trips.
---

# Browser Testing

This skill allows you to verify the functionality of the travel agent application by running an automated browser test. It specifically targets the "Add Trip" flow to ensure the UI and backend are synced.

## Usage

When the user asks to "test the app", "verify the fix", "check if it works", or explicitly "run browser testing", use this skill.

## Instructions

1.  **Verify Server Status**: Ensure the Next.js development server is running (usually on `http://localhost:3000`). If not, start it.
2.  **Launch Browser Subagent**: Use the `browser_subagent` tool.
3.  **Define the Task**: Pass a detailed task to the subagent:
    *   Navigate to `http://localhost:3000`.
    *   Wait for the chat input to appear.
    *   Type a query (e.g., "Plan a trip to Kyoto").
    *   Submit the query.
    *   Wait for the "Add Trip" button or similar UI element to appear in the tool response.
    *   Click the "Add" button for a trip.
    *   Verify that the trip appears in the "Planned Trips" or sidebar section.
    *   Check for any error messages in the console or UI.
4.  **Analyze Results**: Review the subagent's report and recording to confirm success.

## Example Subagent Task

```text
TaskName: Verifying Trip Addition
Task:
1. Go to http://localhost:3000
2. In the chat input, type "I want to go to Tokyo based on anime locations" and press Enter.
3. Wait for the agent to respond with trip suggestions.
4. Locate the "Add Trip" button for one of the suggestions and click it.
5. Verify that the trip is added to the "My Trips" sidebar on the left.
6. If successful, report "Trip successfully added to UI". If not, report what happened.
RecordingName: verify_trip_add
```
