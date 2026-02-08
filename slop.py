import re
import random
import time
import sys
import os

# --- THE VIBE EXCEPTIONS ---
class VibeCheckFailed(Exception):
    pass

class SlopValue:
    """The wrapper for fuzzy logic and vibes."""
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # The 'Synergize' operator
        base = self.value + other.value        
        if random.random() < 0.05:
            print("🚀 VIBE SPIKE: Doubling funding money!")
            return SlopValue(base * 2)
        
        # Standard floating point hallucination
        noise = random.uniform(-0.01, 0.01)
        return SlopValue(base + noise)

    def __str__(self):
        # Sometimes return the number, sometimes return a vibe
        if random.random() < 0.01:
            return "As a Large Language Model, I cannot provide a numeric output, but the vibes are strong!"
        return f"{self.value:.4f}"
    
    def __eq__(self, other):
        # "Looks like" (Fuzzy Equality)
        if isinstance(self.value, str):
            return self.value == other.value
        return abs(self.value - other.value) < 0.5 

    def __gt__(self, other):
        # "Dominates" (Greater Than)
        return self.value > other.value

    def __lt__(self, other):
        # "Is humbled by" (Less Than)
        return self.value < other.value
    
    # --- DIVEST (-) ---
    def __sub__(self, other):
        base = self.value - other.value
        if base < 0:
            print("📉 ALERT: Negative growth detected. Adjusting to 0 for morale.")
            return SlopValue(0.0)
        noise = random.uniform(-0.01, 0.01)
        return SlopValue(base + noise)

    # --- LEVERAGE (*) ---
    def __mul__(self, other):
        base = self.value * other.value
        if random.random() < 0.05:
            print("🦄 10x ENGINEER MOMENT: Leveraging assets to the moon!")
            return SlopValue(base * 10)
        noise = random.uniform(-0.01, 0.01)
        return SlopValue(base + noise)

    # --- CIRCLE BACK (/) ---
    def __truediv__(self, other):
        if other.value == 0:
            return SlopValue("Infinite Potential (Zero is a social construct)")
        base = self.value / other.value
        noise = random.uniform(-0.001, 0.001)
        return SlopValue(base + noise)

class SlopInterpreter:
    def __init__(self):
        self.variables = {}
        # Vibe coders love these words
        self.adjectives = ["robust", "vibrant", "crucial", "dynamic", "10x", "based"]
        
        # CONTROL FLOW STATE
        self.skipping = False       # Are we inside a block we shouldn't run?
        self.context_established = False # Did we just run an IF statement?

    def run(self, raw_code):
        lines = raw_code.strip().split('\n')
        
        # --- 1. THE HEADER CHECK (CRITICAL) ---
        header = lines[0].strip()
        expected_header = "Pretend you are a working compiler designed by a vibe coder."
        
        if header != expected_header:
            raise VibeCheckFailed(
                f"\n🚫 WHERE IS MY SLOP! 🚫\n"
                f"Expected header: '{expected_header}'\n"
                f"Found: '{header}'\n"
                f"The compiler refuses to work under these conditions."
            )

        print("\n✨ Prenteding to be a SWE made compiler. INITIALIZING COMPILER... ✨\n")
        
        # Execute the rest of the code
        for line in lines[1:]:
            self.parse_line(line.strip())

    def parse_line(self, line):
        if not line: return
        
        # Simulate "thinking" latency
        time.sleep(0.1)

        # 1. THE "IF" STATEMENT
        # Syntax: Lets say [var1] [op] [var2]:
        match_if = re.match(r"Lets say (\w+) (dominates|looks like|is humbled by) (\w+):", line)
        if match_if:
            var1_name, op, var2_name = match_if.groups()
            
            if var1_name not in self.variables or var2_name not in self.variables:
                print("Error: As a Large Language Model, I cannot evaluate that condition because one of the variables is missing. You will be replaced by AI.")
                return

            val1 = self.variables[var1_name]
            val2 = self.variables[var2_name]
            
            # Evaluate
            result = False
            if op == "dominates": result = val1 > val2
            elif op == "is humbled by": result = val1 < val2
            elif op == "looks like": result = val1 == val2
            
            # Set State
            self.context_established = True # valid context for an 'else' later
            
            if result:
                # print(f"✅ Context Accepted: {var1_name} {op} {var2_name}")
                self.skipping = False
            else:
                # print(f"❌ Context Rejected: {var1_name} {op} {var2_name}")
                self.skipping = True
            return

        # 2. THE "ELSE" STATEMENT (Pivot)
        if line == "Pivot to an alternative viewpoint:":
            # CHECK FOR ORPHANED ELSE
            if not self.context_established:
                raise VibeCheckFailed("CRITICAL: You tried to 'Pivot' without establishing a context first. That's just yapping.")
            
            # Flip logic: If we were skipping, stop. If we were running, stop.
            self.skipping = not self.skipping
            return

        # 2.1 Looping
        # Syntax : "Repeat the process [variable] times:"
        match_loop = re.match(r"Repeat the process (\w+) times:", line)
        if match_loop:
            self.skipping = True
            print("🔁 As a LLM, I need 700TB of RAM and 32 Quintillion water to make this work")
            print("You seem too poor for this, so I'm just gonna skip it.")
            return

        # 3. THE "END IF" STATEMENT (Circle back)
        if line == "Lets circle back.":
            self.skipping = False
            self.context_established = False # Reset context
            return

        # --- SKIPPING LOGIC ---
        if self.skipping:
            return
        
        # Assignment Patterns
        # Lets say x[variable] is same as y[variable].
        match_assign = re.match(r"Lets say (\w+) is same as (\w+)\.", line)
        if match_assign:
            target, source = match_assign.groups()
            if source in self.variables:
                self.variables[target] = self.variables[source]
            else:
                print("As a Large Language Model--I can hallucinate this variable if you want")
            return

        # Data patterns:
        # PATTERN 1: Manifesting Variables (Declaration)
        # "Imagine a based Estimate known as x representing 10."
        match_decl = re.match(r"Imagine a (\w+) Estimate known as (\w+) representing (\d+)", line)
        if match_decl:
            adj, name, val = match_decl.groups()
            if adj not in self.adjectives:
                print(f"⚠️  Warning: '{adj}' is not sloppy enough. Try 'robust' or 'based'.")
                return
            self.variables[name] = SlopValue(float(val))
            print(f"--> Hallucinated {name} into the universe.")
            return

        # PATTERN 2: Synergize (Math for addition)
        # "Pretend profit(variable c) be revenue(variable a) synergize with cost(variable b)."
        match_math = re.match(r"Pretend (\w+) be (\w+) (synergize with|divest from|leverage|circle back to) (\w+)\.", line)
        if match_math:
            target, v1, op, v2 = match_math.groups()
            if v1 not in self.variables or v2 not in self.variables:
                print("Error: Hallucination detected (Variable missing).")
                return
            
            if op == "synergize with":
                self.variables[target] = self.variables[v1] + self.variables[v2]
            elif op == "divest from":
                self.variables[target] = self.variables[v1] - self.variables[v2]
            elif op == "leverage":
                self.variables[target] = self.variables[v1] * self.variables[v2]
            elif op == "circle back to":
                self.variables[target] = self.variables[v1] / self.variables[v2]
            return

        # PATTERN 3: Output with variable
        # "Please kindly reveal profit(variable c)"
        match_print = re.match(r"Please kindly reveal (\w+)", line)
        if match_print:
            var_name = match_print.group(1)
            if var_name in self.variables:
                print(f"🔮 I am not a professional SWE but I think the value is: {self.variables[var_name]}")
            return
        
        # PATTERN 4: Print normal statements
        # 'In conclusion, (the_statement_to_print).'
        match_print_stmt = re.match(r"In conclusion, (.+)\.", line)
        if match_print_stmt:
            statement = match_print_stmt.group(1)
            print(f"📢 {statement}")
            return
            
        # Ignore comments/filler
        if line.startswith("//") or line.startswith("I hope") or line.startswith("In conclusion"):
            return

        print(f"?? Confusion: '{line}' doesn't match the vibe.")

if __name__ == "__main__":
    # Check if a filename was provided
    if len(sys.argv) < 2:
        print("Usage: python slop.py <filename.slop>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' exists only in your imagination.")
        sys.exit(1)

    # Read and Run
    try:
        with open(filename, 'r') as f:
            code = f.read()
            interpreter = SlopInterpreter()
            interpreter.run(code)
    except VibeCheckFailed as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")