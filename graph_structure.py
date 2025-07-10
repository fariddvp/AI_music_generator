
# Import required libraries
from MusicState import MusicState
from langgraph.graph import StateGraph, END
from component_functions import melody_generator, harmony_creator, rhythm_analyzer, style_adapter, midi_converter
from graphviz import Source
from IPython.display import Image
import shutil

# Initialize the StateGraph
workflow = StateGraph(MusicState)

# Add nodes to the graph
workflow.add_node("melody_generator", melody_generator)
workflow.add_node("harmony_creator", harmony_creator)
workflow.add_node("rhythm_analyzer", rhythm_analyzer)
workflow.add_node("style_adapter", style_adapter)
workflow.add_node("midi_converter", midi_converter)

# Set the entry point of the graph
workflow.set_entry_point("melody_generator")

# Add edges to connect the nodes
workflow.add_edge("melody_generator", "harmony_creator")
workflow.add_edge("harmony_creator", "rhythm_analyzer")
workflow.add_edge("rhythm_analyzer", "style_adapter")
workflow.add_edge("style_adapter", "midi_converter")
workflow.add_edge("midi_converter", END)

# Compile the graph
app = workflow.compile()


# Define input parameters
inputs = {
    "musician_input": "Create a sad violin piece in C major",
    "style": "Classic era"
}

# Invoke the workflow
result = app.invoke(inputs)

print("Composition created")
print(f"MIDI file saved at: {result['midi_file']}")




# Define the destination path where you want to save the MIDI file
destination_path = "saved_music_piece.mid"

# Move the generated MIDI file to the desired location
shutil.move(result["midi_file"], destination_path)

print(f"MIDI file has been saved to: {destination_path}")




# Export the workflow to a DOT file
dot_file_path = "workflow.dot"
workflow.export_graphviz(dot_file_path)

# Render the DOT file to an image
graph = Source.from_file(dot_file_path)
graph.format = "png"
graph.render("workflow", cleanup=True)

# Display the workflow diagram in Colab
Image("workflow.png")

