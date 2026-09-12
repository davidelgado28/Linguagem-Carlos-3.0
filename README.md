# Carlos Programming Language 

Carlos is a modern, strongly-typed programming language that combines the heart and raw performance of C++ with the clean, readable syntax of Python. It enforces strict indentation, removes semicolons, and simplifies types.

## Features
* **No Semicolons**: Statement ends at the end of the line.
* **Golden Rule Indentation**: Blocks inside `{}` must be properly indented, or the compiler will throw an error.
* **Simplified Types**: `float` is removed to avoid redundancy; `double` is the absolute standard.
* **Native Match-Case**: Clean `match(var)` syntax.
* **Super-library**: Comes with `<carlinho.h>` mapping native C++ data structures (like maps, sets, and vectors).

## Repository Structure
* `src/`: Contains the Carlos to C++ transpiler written in Python.
* `include/`: Contains the `carlinho.h` core header.
* `.github/workflows/`: CI/CD pipeline to auto-build the compiler via PyInstaller.

## How to Build the Compiler
If you don't want to download the pre-compiled binary from the GitHub Actions Artifacts, you can build it yourself:

1. Clone this repository.
2. Install requirements: `pip install -r requirements.txt`
3. Build with PyInstaller: `pyinstaller --onefile src/transpiler.py --name carlos-compiler`

## Usage

Create a file named `hello.crl`:

```cpp
#include <carlinho.h>
using namespace facilitador

int main() {
    string msg = "Hello from Carlos!"
    cout << msg << "\n"
    
    for (int i = 0, i < 3, i++) {
        cout << i << "\n"
    }
    
    return 0
}
