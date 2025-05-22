# import os
# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# from .models import Images
# import cv2
# import pytesseract as pyro
# import subprocess
# from PIL import Image

# img1_path = ""
# word_sug1 = ""  # Initialize word_sug1 here

# def index(request):
#     return render(request, 'upload/index.html')

# def uploaded(request):
#     if request.method == 'POST' and 'image' in request.FILES:
#         uploaded_file = request.FILES['image']
#         fs = FileSystemStorage()
#         saved_file = fs.save(uploaded_file.name, uploaded_file)
#         print("Uploaded file:", uploaded_file.name)
#         print("Content type:", uploaded_file.content_type)
#         print("Size:", uploaded_file.size)
#         pa = fs.path(saved_file)
#         print("File path:", pa)

#         s = Images.objects.create(img_name=uploaded_file.name, img_path=pa)
#         print("objects:",s)
#         print("path to ocr:",pa)
#         img1_path = s.img_path
#         print(img1_path)

#         img = Image.open(pa)
#         print(img)
#         #cvvs=cv2.imread(img)

#         textcod = pyro.image_to_string(img)
#         print(textcod)
#         s.img_content = textcod
#         s.save()

#         text = textcod.split('\n')
#         print(text)
#     else:
#         text = []
#         img1_path = ""

#     # Move the definition of word_sug1 here
#     word_sug1 = []

#     def lcs(s1, s2):
#         m, n = len(s1), len(s2)
#         prev, cur = [0] * (n + 1), [0] * (n + 1)
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if s1[i - 1] == s2[j - 1]:
#                     cur[j] = 1 + prev[j - 1]
#                 else:
#                     if cur[j - 1] > prev[j]:
#                         cur[j] = cur[j - 1]
#                     else:
#                         cur[j] = prev[j]
#             cur, prev = prev, cur
#         return prev[n]

#     res_list = ['main', '#include', 'alignas', 'double', 'reinterpret_cast', 'alignof', 'dynamic_cast', 'requires', 'and', 'else', 'return', 'and_eq', 'enum', 'short', 'asm', 'explicit', 'signed', 'atomic_cancel', 'export', 'sizeof', 'atomic_commit', 'extern', 'static', 'atomic_noexcept', 'false', 'static_assert', 'auto', 'float', 'static_cast', 'bitand', 'for', 'struct', 'bitor', 'friend', 'switch', 'bool', 'goto', 'synchronized', 'break', 'if', 'template', 'case', 'import', 'this', 'catch', 'inline', 'thread_local', 'char', 'int', 'throw', 'char16_t', 'long', 'true', 'char32_t', 'module', 'try', 'class', 'mutable', 'typedef', 'compl', 'namespace', 'typeid', 'concept', 'new', 'typename', 'const', 'noexcept', 'union', 'constexpr', 'not', 'unsigned', 'const_cast', 'not_eq', 'using', 'continue', 'nullptr ', 'virtual', 'co_await ', 'operator', 'void', 'co_return', 'or', 'volatile', 'co_yield', 'or_eq', 'wchar_t', 'decltype', 'private', 'while', 'default', 'protected', 'xor', 'delete', 'public', 'xor_eq', 'do', 'register', '<iostream>', 'std', 'cout', 'cin']  

#     def find_suggestion(word, res_list):
#         ans = []
#         lw = len(word)
#         for i in res_list:
#             d = lcs(word, i)
#             if (d * 2 > lw and lw > 2):
#                 ans.append([d, i])
#         ans.sort(reverse=True)
#         final = []
#         for j in ans:
#             final.append(j[1])
#         return final

#     for i in text:
#         g = i.split(' ')
#         if (len(g) != 0):
#             for j in g:
#                 word, wordarr = j, find_suggestion(j.lower(), res_list)
#                 if (len(wordarr) and word != wordarr[0]):
#                     word_sug = [word, " , ".join(wordarr[:min(5, len(wordarr))])]
#                     word_sug1.append(word_sug)

#     return render(request, 'upload/upload.html', {'text': text, 'img1': img1_path, 'suggestion': word_sug1})

# def executed(request):
#     code = ''
#     output = ''
#     img1_path = ''

#     if request.method == 'POST':
#         code = request.POST.get("my_textarea")
      
#         temp_file_path = "E:\\Camcode-master\\Camcode-master\\upload\\sample.cpp" 
#         print(temp_file_path) # Update this path as needed
#         with open(temp_file_path, "w") as f:
#             f.write(code)
#         print("mytextarea:",code)
#         compile_result = subprocess.run(["g++","-o","a.out", temp_file_path], stderr=subprocess.PIPE)
#         print("Return code after compilation:",compile_result.returncode)
#         if compile_result.returncode == 0:
#              print("Compilation successful. Executable file 'a.out' generated.")
#         else:
#             print("Compilation failed. Error message:")
#             print(compile_result.stderr.decode())
#         if compile_result.returncode != 0:
#             output = compile_result.stderr.decode('utf-8')
#         else:
#              try:
#                 execute_result = subprocess.run(["./a.out"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                 print("executed output:", execute_result.stdout.decode())
#                 output = execute_result.stdout.decode()
                
                     
#              except Exception as e:
#                     output = str(e)
#                     print("Error occurred during execution:", output)

#         media_files = os.listdir("E:\Camcode-master\Camcode-master\media")  # Update the path to your media directory
#         if media_files:
#             img1_path = "/media/" + media_files[0]  # Assuming you want the first file in the directory

#     return render(request, 'upload/upload.html', {'text': '', 'code': code, 'output': output, 'img1': img1_path})


import os
import subprocess
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Images
from PIL import Image
import pytesseract as pyro
filepath = r"E:\Camcode-master\Camcode-master\upload\lcs_word.cpp"
def find_suggestion(word):
    # Call the C++ program for word suggestion
    text_words = os.environ.get('TEXT_WORDS', '')  # Word list
    res_list = os.environ.get('RES_LIST', '')  # List of suggestions
    # print("text words",text_words)
    # print("res_list",res_list)
    filepath_cpp = r"E:\Camcode-master\Camcode-master\upload\lcs_word.cpp"
    # cpp_source_file = "lcs_word.cpp"

    # Compile the C++ program into an executable
    compile_result = subprocess.run(["g++", "-o", "lcs_word", filepath_cpp], stderr=subprocess.PIPE)
    print("compileresultcode:",compile_result.returncode)
    if compile_result.returncode == 0:
        print("Compilation successful. Executable 'lcs_word' generated.")
    else:
        print("Compilation failed. Error message:")
        print(compile_result.stderr.decode())
    if compile_result.returncode == 0:
    # Input data to pass to the C++ program

        word = text_words
        # print("The words to c++ program:",word)
        word_list_str = res_list
        # print("the words to c++ program:",word_list_str)

        # Encode input data
        input_data = f"{word}\n{word_list_str}".encode()
        print("input data to the cpp program",input_data)

    # Run the compiled executable using subprocess
        process = subprocess.run(["lcs_word"], input=input_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("process return code of c++ input",process.returncode)
    # Check if the process ran successfully
    if process.returncode == 0:
        print("C++ program executed successfully!")
        # Print the output generated by the C++ program
        #print("Output:")
        output = process.stdout.decode('utf-8')
        # print("The c++ output",output)
        suggestions = process.stdout.splitlines()
        print("the modified c++ output:",suggestions) 
        return suggestions # Return suggestions
        
    else:
        print("Error occurred while running the C++ program:", process.stderr.decode())
    

        

def index(request):
    return render(request, 'upload/index.html')

def uploaded(request):
    img1_path = ""
    img_url=""
    if request.method == 'POST' and 'image' in request.FILES:
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        saved_file = fs.save(uploaded_file.name, uploaded_file)
        # print("Uploaded file:", uploaded_file.name)
        # print("Content type:", uploaded_file.content_type)
        # print("Size:", uploaded_file.size)
        pa = fs.path(saved_file)
        print("File path:", pa)

        s = Images.objects.create(img_name=uploaded_file.name, img_path=pa)
        # print("objects:",s)
        # print("path to ocr:",pa)
        img1_path = s.img_path
        # print(img1_path)
        img_url=fs.url(saved_file)
        img = Image.open(pa)
        # print(img)
        textcod = pyro.image_to_string(img)
        print(textcod)
        s.img_content = textcod
        s.save()

        text = textcod.split('\n')
        print(text)
       
    else:
        text = []
        img1_path = ""
    
    wordarr=[]
    wordarr_disp = []
    word_list_str = ' '.join(text)
    os.environ['TEXT_WORDS'] = word_list_str

    res_list = ['main', '#include', 'alignas', 'double', 'reinterpret_cast', 'alignof', 'dynamic_cast', 'requires', 'and', 'else', 'return', 'and_eq', 'enum', 'short', 'asm', 'explicit', 'signed', 'atomic_cancel', 'export', 'sizeof', 'atomic_commit', 'extern', 'static', 'atomic_noexcept', 'false', 'static_assert', 'auto', 'float', 'static_cast', 'bitand', 'for', 'struct', 'bitor', 'friend', 'switch', 'bool', 'goto', 'synchronized', 'break', 'if', 'template', 'case', 'import', 'this', 'catch', 'inline', 'thread_local', 'char', 'int', 'throw', 'char16_t', 'long', 'true', 'char32_t', 'module', 'try', 'class', 'mutable', 'typedef', 'compl', 'namespace', 'typeid', 'concept', 'new', 'typename', 'const', 'noexcept', 'union', 'constexpr', 'not', 'unsigned', 'const_cast', 'not_eq', 'using', 'continue', 'nullptr ', 'virtual', 'co_await ', 'operator', 'void', 'co_return', 'or', 'volatile', 'co_yield', 'or_eq', 'wchar_t', 'decltype', 'private', 'while', 'default', 'protected', 'xor', 'delete', 'public', 'xor_eq', 'do', 'register', '<iostream>', 'std', 'cout', 'cin','int']
    os.environ['RES_LIST'] = ' '.join(res_list)
    # find_suggestion(word_list_str)
    # print("The output from fucntion:",wordarr)
    for word in word_list_str.split():
        word = word.lower()
        wordarr = find_suggestion(word)
        print("The word array:",wordarr)
        # if wordarr is not None and len(wordarr) > 0 and word != wordarr[0]:
        #     # word_sug = [word, " , ".join(wordarr[:min(5, len(wordarr))])]
        #     word_sug = [word, " , ".join(word for word in wordarr[:min(5, len(wordarr))])]
        #     word_sug1.append(word_sug)
        #     print("The word_sug1:",word_sug1)
        # Assuming 'suggestion' contains the list of dictionaries

       
    for item in wordarr:
        suggestion_str = item.decode('utf-8')  # Convert byte string to regular string
        wordarr_disp.append(suggestion_str)

# Now 'formatted_suggestions' contains the suggestions in the desired format



    return render(request, 'upload/upload.html', {'text': text, 'img1': img_url,'suggestion':wordarr_disp})

def executed(request):
    code = ''
    output = ''
    # img1_path = ''

    if request.method == 'POST':
        code = request.POST.get("my_textarea")
        temp_file_path = "E:\\Camcode-master\\Camcode-master\\upload\\sample.cpp" 
        #print(temp_file_path) # Update this path as needed
        with open(temp_file_path, "w") as f:
            f.write(code)
        #print("mytextarea:",code)
        compile_result = subprocess.run(["g++","-o","a.out", temp_file_path], stderr=subprocess.PIPE)
        print("Return code after compilation:",compile_result.returncode)
        if compile_result.returncode == 0:
             print("Compilation successful. Executable file 'a.out' generated.")
        else:
            print("Compilation failed. Error message:")
           
            print(compile_result.stderr.decode())
           
        if compile_result.returncode != 0:
            output = compile_result.stderr.decode('utf-8')
        else:
             try:
                execute_result = subprocess.run(["./a.out"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print("executed output:", execute_result.stdout.decode())
                output = execute_result.stdout.decode()
                
                     
             except Exception as e:
                    output = str(e)
                    print("Error occurred during execution:", output)

        # media_files = os.listdir("E:\Camcode-master\Camcode-master\media")  # Update the path to your media directory
        # if media_files:
        #     img1_path = "/media/" + media_files[0]  # Assuming you want the first file in the directory
        # print("The image disaplyed :",img1_path)

    return render(request, 'upload/upload.html', {'text': '', 'code': code, 'output': output})


