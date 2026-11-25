"""
generate_modelfiles.py

Creates modelfiles used to establish Ollama models.
Settings are not passed through the command line due to their length. 
The user must edit this file to change the information written to the generated modelfiles.
"""

import os                       # required to find paths.
import argparse                 # command line arguments
import textwrap                 # fix multiline string indents
import errno                    # errors

from main.presets import *      # Take the presets for the main data table from presets.py



def write_to_modelfile(file, model, instruction, parameter_settings):
    """helper function to write to a file"""

    # Create the parameter list first b/c the number of lines may vary
    parameters = [f"PARAMETER {p} {parameter_settings[p]}" for p in parameter_settings.keys()]
    parameters = "\n        ".join(parameters)        

    # f-string into a content variable
    content = f"""\
        # Model
        FROM {model}

        # Parameters
        {parameters}

        # Behavior
        SYSTEM \"\"\"
        {instruction}
        Provide clear, logical, and structured responses to any prompts the user may have.
        Complete the given task to the best of your ability.
        \"\"\""""
    content = textwrap.dedent(content)      # remove whitespace from indents

    # Write to file
    with open(file, "w") as f:
        f.write(content)

        

def generate(path):
    """generates the modelfiles."""
    for model in models.keys():
        for instruction in instructions.keys():
            write_to_modelfile(file=path+f"{model}-{instruction}",
                               model=models[model],
                               instruction=instructions[instruction],
                               parameter_settings=parameters)
        print(f"{len(instructions)} {model} modelfiles written.")
    print("Finished writing instructions; exiting...")





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates Modelfiles based on preset parameters')

    parser.add_argument('-y','--assume_yes', action="store_true", help="automatically agree to warnings")

    parser.add_argument("--path", type=str, default="./modelfiles", help="where to put the completed modelfiles")

    args = parser.parse_args()

    print("Generating modelfiles...")


    if not os.path.isdir(args.path):
        if args.assume_yes:
            print(f"Created directory: {args.path}")
        else:
            if input(f"Create directory? {args.path} [y/n]").lower().strip()=="y":
                pass
            else:
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), str(os.path.abspath(args.path)))
        os.makedirs(args.path)

    
    print(f"Modelfiles saved to: {os.path.abspath(args.path)}")


    print("Using presets.")

    generate(args.path)