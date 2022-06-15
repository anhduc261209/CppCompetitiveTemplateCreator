import sys, time

def main():
    print("--C++ Competitive Template Creator by Anh Duc--")
    try: # Get file name as command line argument
        file_name = sys.argv[1]
    except: # Get file name from input
        file_name = input("Please input file name (include the extension .cpp): ")
    # Write to file
    list_of_lines = ["#include <bits/stdc++.h>\n", "using namespace std;\n", "const int MN = 1e5;\n", "\n", "void ReadData() {\n", "\n", "}\n", "\n", "void Solve() {\n", "\n", "}\n", "\n", "int main() {\n", "\tcin.tie(0)->sync_with_stdio(0);\n", "\n", "\tReadData();\n", "\tSolve();\n", "\n", "\treturn 0;\n", "}"]
    with open(file_name, "w") as f:
        f.writelines(list_of_lines)
    print("File created successfully!")
    time.sleep(60)

if __name__ == '__main__':
    main()
