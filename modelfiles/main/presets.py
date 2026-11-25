"""
presets.py

Presets for Modelfile generation for the main data table.
Also serves as the template for making presets for `generate_modelfiles.py`.
Keep in mind that all file paths will originate from `generate_modelfiles.py`, 
not the location of `presets.py`.
"""





""" ------
| Model names
"""
# Main directory.
# Each dictionary item should be formatted as `"<nickname>" : "<full name>"`.
# The full name can either be an exisitng model to copy weights from, or a GGUF file to use downloaded weights.
models = {
    "qwen"      : "qwen3:8b",
    "ministral" : "ministral-3:8b",
    "llama"     : "llama3:8b"
}


# Path Prefix - appended to the front of every `<full name>` in `models`
# Useful for file paths; ignore if importing from exisitng models.
model_path_prefix = ""





""" ------
| System Instructions
"""
# Instructions variables - defines variables to keep the dictionary below clean.
instr_base      = "You are a helpful, friendly, and highly capable AI assistant."
instr_code      = "You are an advanced computer scientist who specializes in competetive programming."
instr_math      = "You are a brilliant mathematician who specializes in solving competetive math problems."
instr_english   = "You are a knowlegable English teacher and tutor who specializes in grading and revising essays."
instr_translate = "You are an accurate translator who specializes in translating between languages."

# Main directory.
# Each dictionary item should be formatted as `"<nickname>" : "<instructions>"`
# Empty or invalid text will not raise an error.
instructions = {
    "base"      : instr_base,
    "code"      : instr_code,
    "math"      : instr_math,
    "english"   : instr_english,
    "translate" : instr_translate
}


# Instructions Prefix - appended to the start of the text for every `<instructions>` in `instructions`
# This can be used to add additional information to the start of the instructions that is the same
# for every model.
instruction_prefix = """"""

# Instructions Suffix - appended to the end of the text for every `<instructions>` in `instructions`
# This can be used to add additional information to the end of the instructions that is the same
# for every model.
instruction_suffix = """
Provide clear, logical, and structured responses to any prompts the user may have.
Complete the given task to the best of your ability.
"""





""" ------
| Parameters
"""
# Main directory.
# Each dictionary item should be formatted as `"<parameter>" : [<value 1>, <value2>, ...]`
# Empty or invalid parameters will not raise an error.
parameters = {
    "temperature" : [0.7],
    "num_ctx"     : [4096],
    "seed"        : [1]
}