import random
     from supabase import create_client, Client

     # تهيئة Supabase Client
     url = "https://YOUR_SUPABASE_URL.supabase.co"
     key = "YOUR_SUPABASE_KEY"
     supabase: Client = create_client(url, key)

     # إنشاء 30,000 رمز عشوائي مكون من 11 رقمًا
     def generate_code():
         return ''.join([str(random.randint(0, 9)) for _ in range(11)])

     codes = [{"code": generate_code(), "is_used": False} for _ in range(30000)]

     # إضافة الرموز إلى الجدول
     response = supabase.table('codes').insert(codes).execute()

     if response.data:
         print("تم رفع الرموز بنجاح!")
     else:
         print("حدث خطأ أثناء رفع الرموز:", response.error)
اين اضيف هذا الكود
