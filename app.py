from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# إعداد الاتصال بقاعدة البيانات
conn = pymysql.connect(
    host='localhost',
    user='notesuser',
    password='notespass',   # غيري الباسورد لو مختلف عندك
    database='notesdb',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # استخدام get لتجنب KeyError
        note = request.form.get('note')
        if note:  # فقط إذا تم إدخال قيمة
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO notes (content) VALUES (%s)", (note,))
            conn.commit()
        return redirect('/')

    # GET request: جلب الملاحظات مرتبة حديث → قديم
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM notes ORDER BY created_at DESC")
        notes = cursor.fetchall()
    return render_template('index.html', notes=notes)

if __name__ == "__main__":
    # تشغيل التطبيق على كل العناوين و debug mode مفعل
    app.run(host="0.0.0.0", port=5000, debug=True)

