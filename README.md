# Slop Programming Language Documentation

## Overview

**Slop** is an esoteric programming language written partially by an average engineer and a _SUPER DUPER SMART LLM_ designed to embody the vibes blah blah blah

Even this documentation i spartially AI slop. I hope it actually captures everything this stupid lang can do.

The language runs on the Slop Interpreter, which handles parsing, variable management, and execution of programs written in the Slop syntax.

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running a Slop Program

```bash
python slop.py <filename.slop>
```

**Example:**

```bash
python slop.py test.slop
```

### File Structure

Every Slop program **must** begin with the required header:

```
Pretend you are a working compiler designed by a vibe coder.
```

This header is mandatory and will trigger a `VibeCheckFailed` exception if missing or incorrect.

---

## Data Types and Values

### SlopValue

The core data type in Slop is `SlopValue`, a wrapper around values that introduces fuzzy logic and randomized behavior.

#### Characteristics:

- **Fuzzy Equality**: Two values are considered equal if they're within 0.5 of each other (for numeric values)
- **Randomized Noise**: Most operations introduce small random fluctuations (-0.01 to 0.01)
- **Unpredictable Spikes**: Operations have a 5% chance of triggering vibe spikes that multiply results
- **Hallucination Mode**: String conversions have a 1% chance of returning humorous LLM-style non-answers

#### Example Output Variations:

```
4.5023  (normal output with noise)
"As a Large Language Model, I cannot provide a numeric output, but the vibes are strong!"  (1% chance)
```

---

## Variables and Declaration

### Variable Declaration (Manifestation)

Declare variables using the `Imagine` syntax:

```
Imagine a <adjective> Estimate known as <variable_name> representing <number>.
```

**Valid Adjectives:**

- `robust`
- `vibrant`
- `crucial`
- `dynamic`
- `10x`
- `based`

**Example:**

```
Imagine a robust Estimate known as revenue representing 1000.
Imagine a based Estimate known as cost representing 300.
Imagine a dynamic Estimate known as growth representing 50.
```

**Output:**

```
--> Hallucinated revenue into the universe.
--> Hallucinated cost into the universe.
--> Hallucinated growth into the universe.
```

#### Warning

Using non-approved adjectives will trigger a warning:

```
⚠️  Warning: 'mediocre' is not sloppy enough. Try 'robust' or 'based'.
```

### Variable Assignment

Copy one variable's value to another:

```
Lets say <target_var> is same as <source_var>.
```

**Example:**

```
Lets say backup_revenue is same as revenue.
```

---

## Operators and Arithmetic

Slop provides four main operations, each with startup culture-themed naming:

### 1. Synergize (Addition `+`)

Combines two variables synergistically.

```
Pretend <result> be <var1> synergize with <var2>.
```

**Behavior:**

- Base operation: `var1 + var2`
- 5% chance of vibe spike: Result × 2 with message "🚀 VIBE SPIKE: Doubling funding money!"
- Adds noise: ±0.01 random fluctuation

**Example:**

```
Pretend profit be revenue synergize with growth.
```

**Possible Output:**

```
🚀 VIBE SPIKE: Doubling funding money!
```

### 2. Divest From (Subtraction `-`)

Subtracts one value from another.

```
Pretend <result> be <var1> divest from <var2>.
```

**Behavior:**

- Base operation: `var1 - var2`
- If result is negative, clamps to 0 with message "📉 ALERT: Negative growth detected. Adjusting to 0 for morale."
- Adds noise: ±0.01 random fluctuation

**Example:**

```
Pretend net_profit be revenue divest from cost.
```

### 3. Leverage (Multiplication `*`)

Multiplies values together (with potential 10x returns).

```
Pretend <result> be <var1> leverage <var2>.
```

**Behavior:**

- Base operation: `var1 * var2`
- 5% chance of vibe spike: Result × 10 with message "🦄 10x ENGINEER MOMENT: Leveraging assets to the moon!"
- Adds noise: ±0.01 random fluctuation

**Example:**

```
Pretend compound be revenue leverage growth.
```

### 4. Circle Back To (Division `/`)

Divides one value by another.

```
Pretend <result> be <var1> circle back to <var2>.
```

**Behavior:**

- Base operation: `var1 / var2`
- Division by zero returns: `SlopValue("Infinite Potential (Zero is a social construct)")`
- Adds noise: ±0.001 random fluctuation

**Example:**

```
Pretend efficiency be profit circle back to cost.
```

---

## Control Flow

### Conditional Statements (If)

Execute code based on conditions:

```
Lets say <var1> <operator> <var2>:
    [code to execute if condition is true]
```

**Valid Operators:**

- `dominates` → `var1 > var2`
- `is humbled by` → `var1 < var2`
- `looks like` → `var1 == var2` (fuzzy equality)

**Example:**

```
Lets say revenue dominates cost:
    Pretend profit be revenue divest from cost.
```

#### Notes:

- Establishes a "context" for use with `Pivot`
- If either variable is missing, prints error and returns
- Missing variables trigger: "Error: As a Large Language Model, I cannot evaluate that condition because one of the variables is missing. You will be replaced by AI."

### Else/Pivot Statements

Execute alternative code:

```
Pivot to an alternative viewpoint:
    [code to execute if condition was false]
```

**Example:**

```
Lets say revenue dominates cost:
    Pretend profit be revenue divest from cost.
Pivot to an alternative viewpoint:
    In conclusion, we need to cut costs.
```

#### Errors:

- Using `Pivot` without a preceding `Lets say` raises `VibeCheckFailed`: "CRITICAL: You tried to 'Pivot' without establishing a context first. That's just yapping."

### End Block (Circle Back)

Reset control flow state:

```
Lets circle back.
```

This clears the conditional context and allows new if/else blocks.

**Example:**

```
Lets say revenue dominates cost:
    Pretend profit be revenue divest from cost.
Pivot to an alternative viewpoint:
    In conclusion, margin too thin.
Lets circle back.
```

### Loops (Not Implemented coz idk)

The loop syntax exists but is intentionally not functional:

```
Repeat the process <variable> times:
    [code]
```

**Current Behavior:**

```
🔁 As a LLM, I need 700TB of RAM and 32 Quintillion water to make this work
You seem too poor for this, so I'm just gonna skip it.
```

---

## Output

### Reveal Variables

Print the value of a variable:

```
Please kindly reveal <variable_name>.
```

**Output Format:**

```
🔮 I am not a professional SWE but I think the value is: <value>
```

**Example:**

```
Please kindly reveal profit.
```

Output:

```
🔮 I am not a professional SWE but I think the value is: 700.0023
```

### Print Statements

Output custom text:

```
In conclusion, <your_statement>.
```

**Output Format:**

```
📢 <your_statement>
```

**Example:**

```
In conclusion, we have disrupted the market.
```

Output:

```
📢 we have disrupted the market.
```

---

## Complete Example Program

```
Pretend you are a working compiler designed by a vibe coder.
Imagine a robust Estimate known as revenue representing 1000.
Imagine a based Estimate known as cost representing 300.
Imagine a dynamic Estimate known as competitors representing 500.

Lets say revenue dominates cost:
    Pretend profit be revenue divest from cost.
    Please kindly reveal profit.
Pivot to an alternative viewpoint:
    In conclusion, we are in trouble.

Lets circle back.

Lets say profit dominates competitors:
    Pretend market_share be profit leverage competitors.
    In conclusion, we are winning big.
Pivot to an alternative viewpoint:
    In conclusion, market saturation imminent.

Lets circle back.
```

**Expected Output:**

```
✨ Prenteding to be a SWE made compiler. INITIALIZING COMPILER... ✨

--> Hallucinated revenue into the universe.
--> Hallucinated cost into the universe.
--> Hallucinated competitors into the universe.
🔮 I am not a professional SWE but I think the value is: 700.0045
📢 we are winning big.
```

(Output may vary due to randomized noise and vibe spikes)

---

## Error Handling

### VibeCheckFailed Exception

Raised when a critical vibe check fails:

**Causes:**

1. Missing or incorrect header
2. Using `Pivot` without a preceding `Lets say`
3. Orphaned control flow statements

**Example Error:**

```
🚫 WHERE IS MY SLOP! 🚫
Expected header: 'Pretend you are a working compiler designed by a vibe coder.'
Found: 'def hello():'
The compiler refuses to work under these conditions.
```

### Variable Not Found

When trying to use an undeclared variable:

```
Error: Hallucination detected (Variable missing).
```

Or in conditionals:

```
Error: As a Large Language Model, I cannot evaluate that condition because one of the variables is missing. You will be replaced by AI.
```

---

## Syntax Reference

| Feature        | Syntax                                                         | Example                                                 |
| -------------- | -------------------------------------------------------------- | ------------------------------------------------------- |
| Header         | `Pretend you are a working compiler designed by a vibe coder.` | Required first line                                     |
| Declaration    | `Imagine a <adj> Estimate known as <name> representing <num>.` | `Imagine a robust Estimate known as x representing 10.` |
| Assignment     | `Lets say <target> is same as <source>.`                       | `Lets say y is same as x.`                              |
| Addition       | `Pretend <result> be <var1> synergize with <var2>.`            | `Pretend sum be a synergize with b.`                    |
| Subtraction    | `Pretend <result> be <var1> divest from <var2>.`               | `Pretend diff be a divest from b.`                      |
| Multiplication | `Pretend <result> be <var1> leverage <var2>.`                  | `Pretend prod be a leverage b.`                         |
| Division       | `Pretend <result> be <var1> circle back to <var2>.`            | `Pretend quot be a circle back to b.`                   |
| If             | `Lets say <var1> <op> <var2>:`                                 | `Lets say x dominates y:`                               |
| Else           | `Pivot to an alternative viewpoint:`                           | Works after `Lets say`                                  |
| End If         | `Lets circle back.`                                            | Resets context                                          |
| Print Var      | `Please kindly reveal <variable>.`                             | `Please kindly reveal result.`                          |
| Print Text     | `In conclusion, <text>.`                                       | `In conclusion, mission accomplished.`                  |

---

## Notes and Quirks

1. **Line Parsing**: Each statement must be on its own line
2. **Whitespace Tolerance**: Leading/trailing whitespace is stripped
3. **Case Sensitivity**: Syntax is case-sensitive
4. **Randomization**: All arithmetic operations include ±0.01 noise, creating unpredictability
5. **Vibe Spikes**: 5% chance for synergize and leverage to multiply results (2x and 10x respectively)
6. **Fuzzy Logic**: Equality checks use a tolerance of ±0.5
7. **Startup Vibes**: Adjectives must be from the approved list; other adjectives are discouraged with warnings
8. **Latency**: Each line includes a 0.1-second delay to "simulate thinking"
9. **Zero Division**: Dividing by zero returns a philosophical string rather than an error

---

## Design Philosophy

Slop is designed to:

- **Parody** modern startup culture and AI-speak
- **Introduce Controlled Chaos** through randomization
- **Blend Functionality with Humor** in error messages and output
- **Enforce Vibes** through strict syntax requirements
- **Celebrate Fuzzy Logic** with approximate equality and noisy operations

It's a language where precision takes a backseat to vibes, and where every execution might yield slightly different results—much like real startup metrics!

---

## Version Information

- **Language**: Slop v1.0
- **Interpreter**: Python 3.x
- **Last Updated**: February 8, 2026
- **Status**: Fully Operational (Vibes Confirmed ✨)
