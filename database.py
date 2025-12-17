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