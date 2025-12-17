# # ==============================================================================
# #           SQL TILLARI GURUHLARI (DDL, DML, DCL, TCL)
# # ==============================================================================
#
# # 1. DDL (Data Definition Language) - "Tuzilma tili"
# # Vazifasi: Jadvalning o'zini, ustunlarini va bazani yaratish/o'zgartirish.
# # - CREATE: Yangi jadval yoki baza yaratish.
# # - ALTER: Mavjud jadval tuzilishini o'zgartirish (ustun qo'shish/o'chirish).
# # - DROP: Jadvalni butunlay o'chirib tashlash.
# # - TRUNCATE: Jadval ichini bo'shatish (lekin jadval o'zi qoladi).
#
# # 2. DML (Data Manipulation Language) - "Ma'lumot tili"
# # Vazifasi: Jadval ichidagi ma'lumotlar (qatorlar) bilan ishlash.
# # - INSERT: Yangi ma'lumot qo'shish.
# # - UPDATE: Mavjud ma'lumotni tahrirlash.
# # - DELETE: Ma'lumotni o'chirish.
#
# # 3. DQL (Data Query Language) - "So'rov tili"
# # Vazifasi: Ma'lumotlarni bazadan o'qib olish (eng ko'p ishlatiladigan qism).
# # - SELECT: Ma'lumotlarni tanlash va ko'rish.
# # *Eslatma: Ba'zan SELECT ham DML ichiga kiritiladi.
#
# # 4. DCL (Data Control Language) - "Boshqaruv tili"
# # Vazifasi: Foydalanuvchilarga ruxsat berish yoki cheklash.
# # - GRANT: Ruxsat berish (masalan, jadvalni ko'rishga).
# # - REVOKE: Berilgan ruxsatni qaytib olish.
#
# # 5. TCL (Transaction Control Language) - "Tranzaksiya tili"
# # Vazifasi: DML amallarini saqlash yoki bekor qilishni boshqarish.
# # - COMMIT: Bajarilgan amallarni bazaga doimiy saqlash.
# # - ROLLBACK: Xato bo'lsa, amallarni ortga qaytarish (bekor qilish).
# # - SAVEPOINT: Tranzaksiya ichida "to'xtash nuqtasi" yaratish.
#
# # ==============================================================================
# #                             XULOSA JADVALI
# # ==============================================================================
# # Guruh | O'zbekcha nomi     | Ob'ekti           | Asosiy buyruqlar
# # ------|--------------------|-------------------|------------------------------
# # DDL   | Tuzilma tili       | Jadval, Baza      | CREATE, ALTER, DROP
# # DML   | Ma'lumot tili      | Qatorlar (Yozuv)  | INSERT, UPDATE, DELETE
# # DQL   | So'rov tili        | Natijalar         | SELECT
# # DCL   | Nazorat tili       | Huquqlar          | GRANT, REVOKE
# # TCL   | Tranzaksiya tili   | Jarayonlar        | COMMIT, ROLLBACK
# # ==============================================================================
# ==============================================================================
#                 SQL SO'ROVLARINING MANTIQIY BAJARILISH TARTIBI
# ==============================================================================

# SQL so'rov bandlarining to'g'ri (mantiqiy) bajarilish ketma-ketligi:
# FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> DISTINCT -> ORDER BY -> LIMIT

# 1. FROM (Bajarilish tartibi: 1)
#    - Vazifasi: Ma'lumotlar qaysi jadval(lar)dan olinishini aniqlash (ma'lumotlar to'plamining boshlang'ich nuqtasi).

# 2. WHERE (Bajarilish tartibi: 2)
#    - Vazifasi: Individual qatorlarni (yozuvlarni) filtrlash. Guruhlashdan avval har bir yozuvga shart qo'yiladi.
#    - Eslatma: WHERE bandida COUNT, SUM kabi jamlash funksiyalari ishlatilmaydi.

# 3. GROUP BY (Bajarilish tartibi: 3)
#    - Vazifasi: Filtrdan o'tgan qatorlarni ko'rsatilgan ustunlar bo'yicha mantiqiy guruhlarga ajratish.

# 4. HAVING (Bajarilish tartibi: 4)
#    - Vazifasi: GROUP BY natijasida hosil bo'lgan GURUHLARGA shart qo'yish (COUNT > 10 kabi jamlash shartlari).
#    - Eslatma: HAVING faqat jamlangan (aggregate) natijalarni filtrlaydi.

# 5. SELECT (Bajarilish tartibi: 5)
#    - Vazifasi: Ma'lumotlar filtrlangan va guruhlanganidan keyin qaysi ustunlar ko'rsatilishini tanlash.
#    - Eslatma: SELECT so'rovning boshida yozilsa ham, mantiqan keyinroq bajariladi.

# 6. DISTINCT (Bajarilish tartibi: 6)
#    - Vazifasi: SELECT bandi tomonidan tanlangan ustunlar bo'yicha takrorlanuvchi (dublikat) qiymatlarni olib tashlash.

# 7. ORDER BY (Bajarilish tartibi: 7)
#    - Vazifasi: Yakuniy natijalar to'plamini ko'rsatilgan ustun(lar) bo'yicha tartiblash (ASC/DESC).

# 8. LIMIT (Bajarilish tartibi: 8)
#    - Vazifasi: Tartiblangan natijalar to'plamidan faqat ko'rsatilgan eng yuqori sonli qatorlarni chiqarish.

# ==============================================================================

# ==============================================================================
#                 MA'LUMOTLAR BAZASI (DB) ASOSIY NAZARIYASI
# ==============================================================================

# A. ASOSIY TUZILMA VA KOMPONENTLAR

# 1. DATABASE: Ma'lumotlar to'plami. DBMS (PostgreSQL) tomonidan boshqariladi.
# 2. TABLE (Jadval): Ma'lumotlar saqlanadigan asosiy birlik.
# 3. ROW (Qator/Yozuv): Bir ob'ektning barcha ma'lumotlari (Masalan, bitta mijoz).
# 4. COLUMN (Ustun): Ma'lumotlarning bir turi (Masalan, Ism, Narx).

# B. USTUNNI SHAKLLANTIRUVCHI 3 ASOSIY QISM

# 1. Nomi: product_name, customer_id.
# 2. Turi (Data Type): INTEGER (son), VARCHAR (matn), DATE (sana).
# 3. Cheklovlar (Constraints): Ma'lumot sifati uchun qoidalar.

# C. ASOSIY CHEKLOVLAR (CONSTRAINTS)

# 1. PRIMARY KEY: Yozuvning noyob identifikatori. Takrorlanmas (UNIQUE) va bo'sh emas (NOT NULL).
# 2. FOREIGN KEY: Jadvallar orasidagi bog'lanishni o'rnatadi. Boshqa jadvallardagi PK ga ishora qiladi.
# 3. NOT NULL: Bu ustunga qiymat kiritish majburiy.
# 4. UNIQUE: Qiymat takrorlanmasligi shart.

# D. JADVALLAR ORASIDAGI MUNOSABAT (RELATIONS)

# 1. 1:N (Birga-Ko'p): Eng keng tarqalgan. Bir mijoz -> Ko'p buyurtma.

# E. NORMALIZATSIYA
# - Maqsad: Ma'lumotlarning takrorlanishini (Duplication) kamaytirish va ma'lumotlar yaxlitligini oshirish.

# ==============================================================================
#                 SQL SO'ROVINING MANTIQIY BAJARILISHI (CLAUSES)
# ==============================================================================

# Mantiqiy Tartib: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT

# 1. FROM: Qaysi jadvaldan ma'lumot olishni aniqlaydi.
# 2. WHERE: Individual qatorlarni shart asosida filtrlash (GROUP BY dan avval).
# 3. GROUP BY: Qatorlarni guruhlarga birlashtirish.
# 4. HAVING: Guruhlangan natijalarni filtrlash (COUNT, SUM kabi aggregate funksiyalar bilan ishlaydi).
# 5. SELECT: Natija uchun qaysi ustunlar va jamlangan qiymatlar ko'rsatilishini tanlash (mantiqan oxirga yaqin).
# 6. ORDER BY: Yakuniy natijani tartiblash.
# 7. LIMIT: Tartiblangan natijadan faqat yuqori N qatorni olish.

# F. ASOSIY JOIN TURLARI
# 1. INNER JOIN: Ikkala jadvalda ham mos keladigan ma'lumotlarni chiqaradi.
# 2. LEFT JOIN: Chap jadvaldagi barchasini, o'ngdagidan mos kelganini chiqaradi (mos kelmasa NULL).

# ==============================================================================
# ==============================================================================
#           JADVAL YARATISH, O'ZGARTIRISH VA MA'LUMOT QO'SHISH (DDL & DML)
# ==============================================================================

# 1. JADVAL YARATISH (CREATE TABLE)
# Vazifasi: Yangi jadval va uning ustunlarini (column) shakllantirish.
"""
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,    -- SERIAL: Avtomatik o'suvchi ID
    first_name VARCHAR(50) NOT NULL,  -- Ism majburiy
    last_name VARCHAR(50),            -- Familiya
    age INTEGER CHECK (age > 0),      -- Yosh faqat musbat bo'lishi shart
    email VARCHAR(100) UNIQUE,        -- Email takrorlanmasligi shart
    enrolled_date DATE DEFAULT CURRENT_DATE -- Standart qiymat: bugungi sana
);
"""

# 2. BIRDANIGA KO'P MA'LUMOT QO'SHISH (MULTIPLE INSERT)
# Vazifasi: Bitta so'rov bilan jadvalga bir nechta qatorlarni (yozuvlarni) kiritish.
"""
INSERT INTO students (first_name, last_name, age, email)
VALUES 
    ('Ali', 'Valiyev', 20, 'ali@example.com'),
    ('Vali', 'Aliyev', 22, 'vali@example.com'),
    ('Olim', 'Hasanov', 19, 'olim@example.com'),
    ('Zuhra', 'Akramova', 21, 'zuhra@example.com');
"""

# 3. USTUNLARNI BOSHQARISH (ALTER TABLE)
# Vazifasi: Mavjud jadval tarkibiga o'zgartirish kiritish.

# A) Yangi ustun qo'shish:
# ALTER TABLE students ADD COLUMN phone_number VARCHAR(20);

# B) Ustunni o'chirish:
# ALTER TABLE students DROP COLUMN last_name;

# C) Ustun nomini o'zgartirish:
# ALTER TABLE students RENAME COLUMN first_name TO name;

# D) Ustun turini o'zgartirish:
# ALTER TABLE students ALTER COLUMN age TYPE SMALLINT;


# 4. JADVALNI O'CHIRISH (DROP TABLE)
# Vazifasi: Jadvalni barcha ma'lumotlari va tuzilishi bilan birga butunlay yo'q qilish.
# DROP TABLE students;

# 5. JADVAL ICHINI TOZALASH (TRUNCATE)
# Vazifasi: Jadvalni o'zini saqlab qolgan holda, ichidagi barcha qatorlarni o'chirish.
# TRUNCATE TABLE students;

# ==============================================================================