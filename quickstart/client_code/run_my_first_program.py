from nada_dsl import *

def nada_main():
    # Define the parties involved in the computation
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    
    # Define secret integers as inputs from the respective parties
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    
    # Perform addition operation on the secret integers
    result = a + b
    
    # Define the output of the computation, specifying the party to receive it
    return [Output(result, "my_output", party3)]

# Generate the NADA DSL program
nada_program = nada_main().to_program()

# Print the NADA DSL program
print(nada_program)

