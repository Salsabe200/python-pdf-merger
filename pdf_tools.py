import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_filename):
    merger = PdfMerger()
    
    for pdf in pdf_list:
        if os.path.exists(pdf):
            merger.append(pdf)
            print(f"تمت إضافة: {pdf}")
        else:
            print(f"الملف غير موجود: {pdf}")
            
    merger.write(output_filename)
    merger.close()
    print(f"\nتم دمج الملفات بنجاح في: {output_filename}")

# مثال للتجربة (تأكدي من وجود ملفات PDF تجريبية في نفس المجلد)
files_to_merge = ["file1.pdf", "file2.pdf"]
output_pdf = "merged_output.pdf"

# تشغيل عملية الدمج
merge_pdfs(files_to_merge, output_pdf)