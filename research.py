from menu import Note, Notebook
import notebook

print(">>> type(Note) == object\n" + str(isinstance(Note, object)))
print(">>> dir(Note)\n" + str(dir(Note)))
print(">>> type(Notebook) == object\n" + str(isinstance(Notebook, object)))
print(">>> dir(Notebook)\n" + str(dir(Notebook)))


print("\nAbout self: ")
print("Self: " + str(Note.for_res))
print("Type of self: " + str(type(Note.for_res)))