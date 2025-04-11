import aspose.words as aw
from datetime import date

# Загрузить PDF-файлы
PDF1 = aw.Document("main_source.pdf")
PDF2 = aw.Document("main_sourcecheck.pdf")

# Преобразование PDF-файлов в формат Word
PDF1.save("first.docx", aw.SaveFormat.DOCX)
PDF2.save("second.docx", aw.SaveFormat.DOCX)

# Загрузить преобразованные документы Word
DOC1 = aw.Document("first.docx")
DOC2 = aw.Document("second.docx")

# Установить параметры сравнения
options = aw.comparing.CompareOptions()
options.ignore_formatting = True
options.ignore_headers_and_footers = True
options.ignore_case_changes = True
options.ignore_tables = True
options.ignore_fields = True
options.ignore_comments = True
options.ignore_textboxes = True
options.ignore_footnotes = True

# DOC1 будет содержать изменения как редакции после сравнения
DOC1.compare(DOC2, "user", date.today(), options)

if (DOC1.revisions.count > 0):
    # Сохранить полученный файл в формате PDF
    DOC1.save("compared.pdf", aw.SaveFormat.PDF)
else:
    print("Documents are equal")