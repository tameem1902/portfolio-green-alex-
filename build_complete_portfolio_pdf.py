import os
import subprocess
import base64
from pypdf import PdfReader

def get_base64_image(rel_path):
    p = os.path.join(r"c:\Users\Access\Desktop\portfolio green alex", rel_path)
    if os.path.exists(p):
        ext = os.path.splitext(p)[1].lower().replace('.', '')
        if ext == 'jpg': ext = 'jpeg'
        with open(p, 'rb') as f:
            return f"data:image/{ext};base64," + base64.b64encode(f.read()).decode('utf-8')
    return ''

def generate_master_pdf():
    print("Encoding assets to Base64...")
    logo_b64 = get_base64_image("assets/images/logo_clean.png")
    virdiva_b64 = get_base64_image("assets/images/brand_virdiva_showcase.jpg")
    
    # 26 Product images
    prod_imgs = {
        'strawberry': get_base64_image("assets/images/prod_strawberry.jpg"),
        'mango': get_base64_image("assets/images/prod_mango.jpg"),
        'pomegranate': get_base64_image("assets/images/prod_pomegranate.jpg"),
        'figs': get_base64_image("assets/images/prod_figs.jpg"),
        'apricot': get_base64_image("assets/images/prod_apricot.jpg"),
        'green-peas': get_base64_image("assets/images/prod_green_peas.jpg"),
        'green-beans': get_base64_image("assets/images/prod_green_beans.jpg"),
        'okra': get_base64_image("assets/images/prod_okra.jpg"),
        'broccoli': get_base64_image("assets/images/prod_broccoli.jpg"),
        'cauliflower': get_base64_image("assets/images/prod_cauliflower.jpg"),
        'artichoke': get_base64_image("assets/images/prod_artichoke.jpg"),
        'broad-beans': get_base64_image("assets/images/prod_broad_beans.jpg"),
        'spinach': get_base64_image("assets/images/prod_spinach.jpg"),
        'molokhia': get_base64_image("assets/images/prod_molokhia.jpg"),
        'sweet-corn': get_base64_image("assets/images/prod_sweet_corn.jpg"),
        'sweet-peppers': get_base64_image("assets/images/prod_sweet_peppers.jpg"),
        'green-onions': get_base64_image("assets/images/prod_green_onions.jpg"),
        'taro': get_base64_image("assets/images/prod_taro.jpg"),
        'pumpkin': get_base64_image("assets/images/prod_pumpkin.jpg"),
        'sweet-potatoes': get_base64_image("assets/images/prod_sweet_potatoes.jpg"),
        'mixed-peas-carrots': get_base64_image("assets/images/cat_processed.jpg"),
        'mixed-3way': get_base64_image("assets/images/prod_mixed_3way.jpg"),
        'mixed-4way': get_base64_image("assets/images/prod_mixed_4way.jpg"),
        'custom-blends': get_base64_image("assets/images/cat_processed.jpg"),
        'french-fries': get_base64_image("assets/images/prod_french_fries.jpg"),
        'falafel': get_base64_image("assets/images/prod_falafel.jpg"),
    }

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>GREEN ALEX — Comprehensive IQF Product Portfolio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  @page {{
    size: A4 portrait;
    margin: 12mm 14mm 12mm 14mm;
    @bottom-left {{
      content: "GREEN ALEX | Official IQF Product Portfolio";
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 7pt;
      color: #64748b;
      font-weight: 500;
    }}
    @bottom-right {{
      content: "Page " counter(page);
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 7pt;
      color: #64748b;
      font-weight: 700;
    }}
  }}

  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}

  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #0f172a;
    background: #ffffff;
    line-height: 1.35;
    font-size: 8pt;
    margin: 0;
    padding: 0;
  }}

  .arabic {{
    font-family: 'Cairo', sans-serif;
    direction: rtl;
    text-align: right;
  }}

  .doc-page {{
    page-break-after: always;
    height: 272mm;
    max-height: 272mm;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    overflow: hidden;
  }}
  .doc-page:last-child {{
    page-break-after: avoid;
  }}

  /* Page Headers */
  .page-top-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #059669;
    padding-bottom: 6px;
    margin-bottom: 12px;
  }}
  .top-left-brand {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .top-logo-img {{
    height: 26px;
    width: auto;
  }}
  .top-brand-text {{
    font-size: 8.5pt;
    font-weight: 800;
    color: #064e3b;
    letter-spacing: 0.5px;
  }}
  .top-right-meta {{
    font-size: 7pt;
    font-weight: 600;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  /* Typography */
  h1, h2, h3, h4 {{
    margin: 0 0 6px 0;
    color: #064e3b;
    font-weight: 800;
  }}
  .section-title {{
    font-size: 13pt;
    font-weight: 800;
    color: #064e3b;
    display: flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 4px;
  }}
  .section-subtitle {{
    font-size: 7.8pt;
    color: #475569;
    margin-bottom: 10px;
    line-height: 1.3;
  }}
  .badge-tag {{
    display: inline-block;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 6.8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .badge-emerald {{
    background: #ecfdf5;
    color: #047857;
    border: 1px solid #a7f3d0;
  }}
  .badge-gold {{
    background: #fffbeb;
    color: #b45309;
    border: 1px solid #fde68a;
  }}

  /* Tables */
  table.corp-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 10px;
    font-size: 7.6pt;
  }}
  table.corp-table th {{
    background: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    text-align: left;
    padding: 5px 8px;
    border: 1px solid #cbd5e1;
    font-size: 7.2pt;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }}
  table.corp-table td {{
    padding: 5px 8px;
    border: 1px solid #e2e8f0;
    color: #334155;
    vertical-align: middle;
  }}
  table.corp-table tr:nth-child(even) td {{
    background: #f8fafc;
  }}
  .arabic-table th, .arabic-table td {{
    text-align: right;
    direction: rtl;
  }}

  .pill-month {{
    display: inline-block;
    background: #f0fdf4;
    color: #15803d;
    padding: 1.5px 6px;
    border-radius: 3px;
    font-weight: 700;
    font-size: 7pt;
    border: 1px solid #bbf7d0;
  }}

  .notice-box {{
    background: #f8fafc;
    border-left: 3.5px solid #059669;
    padding: 6px 10px;
    border-radius: 0 4px 4px 0;
    margin-bottom: 8px;
    font-size: 7.4pt;
    color: #334155;
  }}
  .notice-box-ar {{
    border-left: none;
    border-right: 3.5px solid #059669;
    border-radius: 4px 0 0 4px;
    direction: rtl;
    text-align: right;
  }}

  /* Cards Grid */
  .gallery-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    margin-top: 6px;
  }}
  .prod-card {{
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    background: #ffffff;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }}
  .prod-card-img {{
    width: 100%;
    height: 92px;
    object-fit: cover;
    background: #f1f5f9;
  }}
  .prod-card-body {{
    padding: 6px 7px;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .prod-name-en {{
    font-size: 7.8pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.15;
  }}
  .prod-name-ar {{
    font-family: 'Cairo', sans-serif;
    font-size: 7.4pt;
    font-weight: 700;
    color: #059669;
    direction: rtl;
    text-align: right;
    margin-bottom: 4px;
  }}
  .prod-styles-tag {{
    font-size: 6.5pt;
    color: #64748b;
    background: #f8fafc;
    padding: 2px 4px;
    border-radius: 3px;
    border: 1px solid #f1f5f9;
    line-height: 1.2;
  }}

  /* Cover Styling */
  .cover-container {{
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 20px 10px 10px 10px;
    background: radial-gradient(circle at 80% 20%, rgba(5, 150, 105, 0.06), transparent 60%);
  }}
  .cover-header {{
    text-align: center;
  }}
  .cover-logo {{
    width: 220px;
    height: auto;
    margin-bottom: 14px;
  }}
  .cover-company-title {{
    font-size: 26pt;
    font-weight: 900;
    color: #064e3b;
    letter-spacing: 1px;
    margin-bottom: 2px;
  }}
  .cover-doc-title {{
    font-size: 14pt;
    font-weight: 800;
    color: #d97706;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
  }}
  .cover-tagline {{
    font-size: 9.5pt;
    color: #475569;
    font-weight: 600;
    margin-bottom: 22px;
  }}
  .cover-grid-stats {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin: 25px 0;
  }}
  .stat-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-top: 3.5px solid #059669;
    padding: 12px 10px;
    text-align: center;
    border-radius: 4px;
  }}
  .stat-card.gold-top {{
    border-top-color: #d97706;
  }}
  .stat-val {{
    font-size: 15pt;
    font-weight: 800;
    color: #0f172a;
  }}
  .stat-lbl {{
    font-size: 7.2pt;
    font-weight: 600;
    color: #64748b;
    margin-top: 2px;
    text-transform: uppercase;
  }}
  .cover-footer {{
    border-top: 1.5px solid #e2e8f0;
    padding-top: 14px;
    font-size: 7.5pt;
    color: #475569;
    line-height: 1.45;
  }}
</style>
</head>
<body>

<!-- ========================================================= -->
<!-- PAGE 1: TITLE & COVER PAGE                                 -->
<!-- ========================================================= -->
<div class="doc-page">
  <div class="cover-container">
    <div class="cover-header">
      <img src="{logo_b64}" class="cover-logo" alt="GREEN ALEX LOGO">
      <div class="cover-company-title">GREEN ALEX</div>
      <div class="cover-doc-title">IQF PRODUCTS PORTFOLIO</div>
      <div class="cover-tagline">Seasonal Harvest Calendar • Product Forms • Quality Standards</div>
      <span class="badge-tag badge-emerald" style="font-size: 8pt; padding: 4px 12px;">OFFICIAL EXPORT CATALOGUE • SEASON 2026 / 2027</span>
    </div>

    <div class="cover-grid-stats">
      <div class="stat-card">
        <div class="stat-val">1999</div>
        <div class="stat-lbl">Established Year</div>
      </div>
      <div class="stat-card gold-top">
        <div class="stat-val">26 Items</div>
        <div class="stat-lbl">Export Products</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">-18°C</div>
        <div class="stat-lbl">Cryogenic Freeze</div>
      </div>
      <div class="stat-card gold-top">
        <div class="stat-val">100% IQF</div>
        <div class="stat-lbl">Natural Quality</div>
      </div>
    </div>

    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px; margin-bottom: 20px;">
      <h3 style="font-size: 9.5pt; color: #064e3b; margin-bottom: 6px;">Executive Procurement & Export Overview</h3>
      <p style="font-size: 7.8pt; color: #334155; margin-bottom: 8px;">
        GREEN ALEX is an established Egyptian food-processing enterprise operating state-of-the-art individually quick frozen (IQF) production lines. Founded in 1999 by Dr. Mohamed Gabr, the company serves international B2B importers, food service distributors, and retail supermarket chains across Europe, North America, the Middle East, and Asia.
      </p>
      <div style="display: flex; justify-content: space-between; font-size: 7.5pt; color: #059669; font-weight: 700;">
        <span>✓ 5 Premium IQF Fruits</span>
        <span>✓ 15 Nile Valley IQF Vegetables</span>
        <span>✓ 6 Ready-to-Cook & Blends</span>
        <span>✓ Private Label & Virdi Va™</span>
      </div>
    </div>

    <div class="cover-footer">
      <div style="display: flex; justify-content: space-between; align-items: flex-end;">
        <div>
          <strong>Founded & Owned by:</strong> Dr. Mohamed Gabr<br>
          <strong>Factory & Commercial Registration:</strong> Rashid, Beheira Governorate, Egypt<br>
          <strong>Administration Office:</strong> 10 Ibn Shogaa Street, Al-Azareeta, Alexandria, Egypt<br>
          <strong>Export Sourcing Desk & WhatsApp:</strong> +20 109 300 3736
        </div>
        <div style="text-align: right;">
          <span class="badge-tag badge-gold">Verified Quality</span><br>
          <span style="font-size: 6.8pt; color: #94a3b8;">Document Revision: November 2026 (v2.0)</span>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ========================================================= -->
<!-- PAGE 2: COMPANY PROFILE (ENGLISH & ARABIC)                  -->
<!-- ========================================================= -->
<div class="doc-page">
  <div class="page-top-bar">
    <div class="top-left-brand">
      <img src="{logo_b64}" class="top-logo-img" alt="logo">
      <span class="top-brand-text">GREEN ALEX</span>
    </div>
    <div class="top-right-meta">Company Profile & Corporate Credentials</div>
  </div>

  <div class="section-title">
    <span>COMPANY PROFILE</span>
    <span class="badge-tag badge-emerald">Established 1999</span>
  </div>
  <p class="section-subtitle">
    GREEN ALEX is an Egyptian food-processing company established in 1999 and founded by Dr. Mohamed Gabr. The company focuses on the processing and supply of individually quick frozen (IQF) fruits and vegetables, alongside selected processed and ready-to-cook products.
  </p>
  <p style="font-size: 7.8pt; color: #334155; margin-bottom: 8px;">
    With a seasonal raw-material approach, GREEN ALEX plans production around optimum crop availability and customer specifications. Product styles, grading, cutting sizes, blends and packing formats can be tailored subject to raw-material availability, approved specifications and production capability.
  </p>

  <table class="corp-table">
    <thead>
      <tr>
        <th style="width: 32%;">Item</th>
        <th style="width: 68%;">Official Details</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>Company Name</strong></td><td><strong>GREEN ALEX (شركة جرين أليكس للحاصلات الزراعية والتصنيع الغذائي)</strong></td></tr>
      <tr><td><strong>Established</strong></td><td>1999 (Over 27 years of agro-processing heritage)</td></tr>
      <tr><td><strong>Founder / Owner</strong></td><td>Dr. Mohamed Gabr (د. محمد جبر)</td></tr>
      <tr><td><strong>Commercial Registration</strong></td><td>Rashid, Beheira Governorate, Egypt (سجل تجاري رشيد – البحيرة)</td></tr>
      <tr><td><strong>Administration Office</strong></td><td>10 Ibn Shogaa Street, Al-Azareeta, Alexandria, Egypt</td></tr>
      <tr><td><strong>Export Desk / WhatsApp</strong></td><td>+20 109 300 3736</td></tr>
    </tbody>
  </table>

  <div style="margin-top: 14px;">
    <div class="section-title arabic" style="justify-content: flex-start;">
      <span>نبذة عن الشركة</span>
      <span class="badge-tag badge-emerald" style="margin-right: 8px;">تأسست عام 1999</span>
    </div>
    <p class="arabic" style="font-size: 8.2pt; color: #334155; line-height: 1.5; margin-bottom: 8px;">
      شركة GREEN ALEX هي شركة مصرية رائدة تأسست عام 1999 على يد الدكتور/ محمد جبر، وتعمل في مجال تجهيز وتصنيع وتوريد منتجات الفواكه والخضروات المجمدة بالتجميد الفردي السريع (IQF)، إلى جانب تشكيلة مختارة من المنتجات المصنعة والجاهزة للطهي.
    </p>
    <p class="arabic" style="font-size: 8.2pt; color: #334155; line-height: 1.5; margin-bottom: 10px;">
      تعتمد الشركة على التخطيط الزراعي الموسمي لتوافر المحاصيل الزراعية عبر محافظات الدلتا والنيل، مع إمكانية تقديم أشكال تصنيع ومقاسات تقطيع ودرجات فرز وخلطات وتعبئة مخصصة وفقاً لمتطلبات العملاء، وبما يتوافق مع توافر الخامات والمواصفات القياسية المعتمدة والطاقة الإنتاجية المتطورة.
    </p>

    <table class="corp-table arabic-table" style="direction: rtl;">
      <thead>
        <tr>
          <th style="width: 32%;">البيان</th>
          <th style="width: 68%;">التفاصيل الرسمية المعتمدة</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>اسم الشركة</strong></td><td><strong>GREEN ALEX (جرين أليكس)</strong></td></tr>
        <tr><td><strong>سنة التأسيس</strong></td><td>1999م</td></tr>
        <tr><td><strong>المؤسس / المالك</strong></td><td>الدكتور/ محمد جبر</td></tr>
        <tr><td><strong>السجل التجاري</strong></td><td>رشيد – محافظة البحيرة، جمهورية مصر العربية</td></tr>
        <tr><td><strong>مقر الإدارة</strong></td><td>10 شارع ابن شجاع، الأزاريطة، الإسكندرية، مصر</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ========================================================= -->
<!-- PAGE 3: PRODUCT PORTFOLIO TABLE (PART 1: ITEMS 1 TO 13)     -->
<!-- ========================================================= -->
<div class="doc-page">
  <div class="page-top-bar">
    <div class="top-left-brand">
      <img src="{logo_b64}" class="top-logo-img" alt="logo">
      <span class="top-brand-text">GREEN ALEX</span>
    </div>
    <div class="top-right-meta">Technical Catalogue — Part 1 (Items 1 to 13)</div>
  </div>

  <div class="section-title">
    <span>IQF PRODUCT PORTFOLIO — PART 1</span>
    <span class="badge-tag badge-gold">26 Products Master Catalogue</span>
  </div>
  <div class="notice-box">
    <strong>Important Commercial Note (Official):</strong> Product forms and cutting sizes below are common commercial options. Final specifications, grading, blend ratios and packaging requirements are agreed with each customer and confirmed through approved product specification sheets and samples.
  </div>

  <table class="corp-table">
    <thead>
      <tr>
        <th style="width: 25%;">Product (EN / AR)</th>
        <th style="width: 12%;">Category</th>
        <th style="width: 28%;">Available Styles</th>
        <th style="width: 22%;">Typical Commercial Sizes</th>
        <th style="width: 13%;">Peak Harvest</th>
      </tr>
    </thead>
    <tbody>
      <!-- FRUITS (5 Products) -->
      <tr style="background: #ecfdf5;">
        <td colspan="5" style="font-weight: 800; color: #047857; font-size: 7.8pt;">A. IQF FRUITS (الفواكه المجمدة) — 5 Products</td>
      </tr>
      <tr>
        <td><strong>Strawberry</strong><br><span class="arabic">فراولة</span></td>
        <td><span class="badge-tag badge-emerald">Fruits</span></td>
        <td>Whole, halves, slices, diced</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Dec – Apr</span></td>
      </tr>
      <tr>
        <td><strong>Mango</strong><br><span class="arabic">مانجو</span></td>
        <td><span class="badge-tag badge-emerald">Fruits</span></td>
        <td>Diced, chunks, slices</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Jul – Oct</span></td>
      </tr>
      <tr>
        <td><strong>Pomegranate arils</strong><br><span class="arabic">حبوب رمان</span></td>
        <td><span class="badge-tag badge-emerald">Fruits</span></td>
        <td>Cleaned whole arils (Ruby red)</td>
        <td>Customer specification / حسب مواصفة العميل</td>
        <td><span class="pill-month">Sep – Dec</span></td>
      </tr>
      <tr>
        <td><strong>Figs</strong><br><span class="arabic">تين</span></td>
        <td><span class="badge-tag badge-emerald">Fruits</span></td>
        <td>Whole, halves, quarters, diced</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Jul – Oct</span></td>
      </tr>
      <tr>
        <td><strong>Apricot</strong><br><span class="arabic">مشمش</span></td>
        <td><span class="badge-tag badge-emerald">Fruits</span></td>
        <td>Halves, quarters, diced</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">May – Jul</span></td>
      </tr>

      <!-- VEGETABLES PART 1 -->
      <tr style="background: #f0fdf4;">
        <td colspan="5" style="font-weight: 800; color: #166534; font-size: 7.8pt;">B. IQF VEGETABLES (الخضروات المجمدة) — Items 6 to 13</td>
      </tr>
      <tr>
        <td><strong>Green peas</strong><br><span class="arabic">بسلة خضراء</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Whole kernels</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Nov – Mar</span></td>
      </tr>
      <tr>
        <td><strong>Green beans</strong><br><span class="arabic">فاصوليا خضراء</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Whole, cut</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Apr – Jul & Oct – Jan</span></td>
      </tr>
      <tr>
        <td><strong>Okra (Bamia)</strong><br><span class="arabic">بامية</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Extra , zero , one , two</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Apr – Oct</span></td>
      </tr>
      <tr>
        <td><strong>Broccoli</strong><br><span class="arabic">بروكلي</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Florets</td>
        <td>Common floret grades 20–60 mm</td>
        <td><span class="pill-month">Oct – Mar</span></td>
      </tr>
      <tr>
        <td><strong>Cauliflower</strong><br><span class="arabic">قرنبيط</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Florets</td>
        <td>Common floret grades 20–60 mm</td>
        <td><span class="pill-month">Oct – Mar</span></td>
      </tr>
      <tr>
        <td><strong>Artichoke</strong><br><span class="arabic">خرشوف</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Hearts, bottoms, quarters</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Oct – Mar</span></td>
      </tr>
      <tr>
        <td><strong>Broad beans (Foul)</strong><br><span class="arabic">فول أخضر</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Peeled, unpeeled</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Nov – Apr</span></td>
      </tr>
      <tr>
        <td><strong>Spinach</strong><br><span class="arabic">سبانخ</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Whole leaf, cut leaf, chopped, minced</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Nov – Mar</span></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ========================================================= -->
<!-- PAGE 4: PRODUCT PORTFOLIO TABLE (PART 2: ITEMS 14 TO 26)    -->
<!-- ========================================================= -->
<div class="doc-page">
  <div class="page-top-bar">
    <div class="top-left-brand">
      <img src="{logo_b64}" class="top-logo-img" alt="logo">
      <span class="top-brand-text">GREEN ALEX</span>
    </div>
    <div class="top-right-meta">Technical Catalogue — Part 2 (Items 14 to 26)</div>
  </div>

  <div class="section-title">
    <span>IQF PRODUCT PORTFOLIO — PART 2</span>
    <span class="badge-tag badge-gold">Vegetables & Processed Range</span>
  </div>

  <table class="corp-table">
    <thead>
      <tr>
        <th style="width: 25%;">Product (EN / AR)</th>
        <th style="width: 12%;">Category</th>
        <th style="width: 28%;">Available Styles</th>
        <th style="width: 22%;">Typical Commercial Sizes</th>
        <th style="width: 13%;">Peak Harvest</th>
      </tr>
    </thead>
    <tbody>
      <!-- VEGETABLES CONTINUED (Items 14 to 20) -->
      <tr style="background: #f0fdf4;">
        <td colspan="5" style="font-weight: 800; color: #166534; font-size: 7.8pt;">B. IQF VEGETABLES (الخضروات المجمدة) — Continued (Items 14 to 20)</td>
      </tr>
      <tr>
        <td><strong>Molokhia</strong><br><span class="arabic">ملوخية</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Minced, chopped, leaf</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">May – Sep</span></td>
      </tr>
      <tr>
        <td><strong>Sweet corn</strong><br><span class="arabic">ذرة حلوة</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Whole kernels, cut cobs, sweet corn half cob and whole cob</td>
        <td>Kernel grade / sweetness per specification</td>
        <td><span class="pill-month">May – Sep</span></td>
      </tr>
      <tr>
        <td><strong>Sweet peppers</strong><br><span class="arabic">فلفل ألوان</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Strips, diced</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Jun – Oct</span></td>
      </tr>
      <tr>
        <td><strong>Green onion and onion</strong><br><span class="arabic">بصل وبصل أخضر</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Whole, cut, diced, chopped rings</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Nov – May</span></td>
      </tr>
      <tr>
        <td><strong>Taro</strong><br><span class="arabic">قلقاس</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Diced</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Oct – Mar</span></td>
      </tr>
      <tr>
        <td><strong>Pumpkin</strong><br><span class="arabic">قرع عسل</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Diced</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Aug – Jan</span></td>
      </tr>
      <tr>
        <td><strong>Sweet potatoes</strong><br><span class="arabic">بطاطا حلوة</span></td>
        <td><span class="badge-tag badge-emerald">Vegetables</span></td>
        <td>Diced, sliced, strips</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Aug – Feb</span></td>
      </tr>

      <!-- PROCESSED & BLENDS (Items 21 to 26) -->
      <tr style="background: #fffbeb;">
        <td colspan="5" style="font-weight: 800; color: #92400e; font-size: 7.8pt;">C. MIXED VEGETABLES & PROCESSED (الخضار المشكل والمصنع) — 6 Products</td>
      </tr>
      <tr>
        <td><strong>Mixed peas & carrots</strong><br><span class="arabic">بسلة وجزر</span></td>
        <td><span class="badge-tag badge-gold">Processed</span></td>
        <td>Whole peas and diced carrots</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Year-Round</span></td>
      </tr>
      <tr>
        <td><strong>Mixed 3-way</strong><br><span class="arabic">خضار مشكل ثلاثي</span></td>
        <td><span class="badge-tag badge-gold">Processed</span></td>
        <td>Whole peas, diced carrots, cut green beans</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Year-Round</span></td>
      </tr>
      <tr>
        <td><strong>Mixed 4-way</strong><br><span class="arabic">خضار مشكل رباعي</span></td>
        <td><span class="badge-tag badge-gold">Processed</span></td>
        <td>Whole peas, diced carrots, cut beans, corn</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Year-Round</span></td>
      </tr>
      <tr>
        <td><strong>Custom blends</strong><br><span class="arabic">خلطات مخصصة</span></td>
        <td><span class="badge-tag badge-gold">Processed</span></td>
        <td>Customized blends to buyer formula</td>
        <td>Ingredients and blend ratios by agreement</td>
        <td><span class="pill-month">Year-Round</span></td>
      </tr>
      <tr>
        <td><strong>French fries</strong><br><span class="arabic">بطاطس نصف مقلية</span></td>
        <td><span class="badge-tag badge-gold">Processed</span></td>
        <td>Straight cut (Par-fried frozen)</td>
        <td>Customer specifications / حسب مواصفات العميل</td>
        <td><span class="pill-month">Year-Round</span></td>
      </tr>
      <tr>
        <td><strong>Falafel (Taameya)</strong><br><span class="arabic">فلافل / طعمية</span></td>
        <td><span class="badge-tag badge-gold">Processed</span></td>
        <td>Balls</td>
        <td>Weight and diameter by agreement</td>
        <td><span class="pill-month">Year-Round</span></td>
      </tr>
    </tbody>
  </table>

  <div class="notice-box notice-box-ar arabic" style="margin-top: 10px;">
    <strong>ملاحظة فنية معتمدة:</strong> أشكال التصنيع ومقاسات التقطيع المذكورة أعلاه هي خيارات تجارية شائعة ومتاحة. يتم الاتفاق على المواصفات النهائية ودرجات الفرز ونسب الخلط واشتراطات التعبئة والتغليف مع كل عميل وتأكيدها عبر بطاقات مواصفات المنتج والعينات المعتمدة رسمياً قبل بدء التشغيل.
  </div>
</div>

<!-- ========================================================= -->
<!-- PAGE 5: PACKAGING FORMATS & LOGISTICS                       -->
<!-- ========================================================= -->
<div class="doc-page">
  <div class="page-top-bar">
    <div class="top-left-brand">
      <img src="{logo_b64}" class="top-logo-img" alt="logo">
      <span class="top-brand-text">GREEN ALEX</span>
    </div>
    <div class="top-right-meta">Packaging Formats & Logistics</div>
  </div>

  <div class="section-title">
    <span>PACKAGING FORMATS & LOGISTICS | أوزان وطرق التعبئة</span>
    <span class="badge-tag badge-emerald">Cold-Chain Standard</span>
  </div>
  <p class="section-subtitle">
    Available packaging formats, export master weights, and customized bulk packaging engineered for maritime reefer containers and supermarket retail distribution.
  </p>

  <h3 style="font-size: 9.5pt; color: #064e3b; margin: 8px 0 4px 0;">Official Packaging Matrix | جدول أوزان وأنظمة التعبئة الرسمية</h3>
  <table class="corp-table">
    <thead>
      <tr>
        <th style="width: 25%;">Packaging Type</th>
        <th style="width: 25%;">نوع التعبئة</th>
        <th style="width: 25%;">Net Weight (EN)</th>
        <th style="width: 25%;">الوزن الصافي (عربي)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Plastic Bags</strong></td>
        <td><strong class="arabic">أكياس</strong></td>
        <td><span class="badge-tag badge-emerald" style="font-size: 7.8pt;">2,500 g</span></td>
        <td><span class="badge-tag badge-emerald arabic" style="font-size: 7.8pt;">٢,٥٠٠ جم</span></td>
      </tr>
      <tr>
        <td><strong>Plastic Bags</strong></td>
        <td><strong class="arabic">أكياس</strong></td>
        <td><span class="badge-tag badge-emerald" style="font-size: 7.8pt;">400 g</span></td>
        <td><span class="badge-tag badge-emerald arabic" style="font-size: 7.8pt;">٤٠٠ جم</span></td>
      </tr>
      <tr>
        <td><strong>Cartons</strong></td>
        <td><strong class="arabic">كراتين</strong></td>
        <td><span class="badge-tag badge-gold" style="font-size: 7.8pt;">10 kg</span></td>
        <td><span class="badge-tag badge-gold arabic" style="font-size: 7.8pt;">١٠ كجم</span></td>
      </tr>
      <tr>
        <td><strong>Woven Sacks</strong></td>
        <td><strong class="arabic">أجولة</strong></td>
        <td><span class="badge-tag badge-emerald" style="font-size: 7.8pt;">25 kg</span></td>
        <td><span class="badge-tag badge-emerald arabic" style="font-size: 7.8pt;">٢٥ كجم</span></td>
      </tr>
    </tbody>
  </table>

  <div class="notice-box" style="margin: 10px 0;">
    <strong>Packaging Flexibility | مرونة التعبئة:</strong><br>
    <em>"Available in different packaging options according to customer requirements and product specifications."</em><br>
    <span class="arabic">"متاحة بأكثر من نظام تعبئة وفقاً لمتطلبات العملاء وطبيعة ومواصفات كل منتج."</span>
  </div>

  <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px; margin-top: 14px;">
    <div style="display: flex; gap: 14px; align-items: center;">
      <img src="{virdiva_b64}" style="width: 140px; height: auto; border-radius: 4px; border: 1px solid #cbd5e1;" alt="Virdi Va Showcase">
      <div>
        <h4 style="color: #064e3b; margin-bottom: 3px;">Virdi Va™ — Approved Retail Packaging Trademark</h4>
        <span class="badge-tag badge-gold" style="margin-bottom: 6px;">Commercial Retail Pouch: 400g</span>
        <p style="font-size: 7.5pt; color: #475569; margin: 0 0 6px 0;">
          GREEN ALEX offers high-barrier printed 400g consumer retail pillow pouches under its proprietary registered brand <strong>Virdi Va™</strong>, alongside full Private Label packaging solutions for international retail chains.
        </p>
        <div style="font-size: 7.2pt; color: #059669; font-weight: 700;">
          Core Retail Products: Green Beans • Green Peas • Diced Carrots • Frozen Strawberries
        </div>
      </div>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-top: 14px;">
    <div style="border: 1px solid #e2e8f0; border-radius: 4px; padding: 8px; background: #ffffff;">
      <strong style="color: #064e3b; font-size: 7.8pt;">Maritime Reefer Logistics</strong>
      <p style="font-size: 7.2pt; color: #64748b; margin: 3px 0 0 0;">
        Export cartons (10 kg net) are packed with food-grade blue polyethylene liners, stacked on EURO / Standard pallets, shrink-wrapped, and containerized at continuous temperature of -18°C or colder.
      </p>
    </div>
    <div style="border: 1px solid #e2e8f0; border-radius: 4px; padding: 8px; background: #ffffff;">
      <strong style="color: #064e3b; font-size: 7.8pt;">Food Service & Industrial Bulk</strong>
      <p style="font-size: 7.2pt; color: #64748b; margin: 3px 0 0 0;">
        Medium-bulk 2,500g poly bags designed for hotel, restaurant and catering (Horeca) efficiency, and 25 kg woven polypropylene sacks for industrial jam, puree, and food manufacturers.
      </p>
    </div>
  </div>
</div>

<!-- ========================================================= -->
<!-- PAGE 6: SEASONAL HARVEST CALENDAR                           -->
<!-- ========================================================= -->
<div class="doc-page">
  <div class="page-top-bar">
    <div class="top-left-brand">
      <img src="{logo_b64}" class="top-logo-img" alt="logo">
      <span class="top-brand-text">GREEN ALEX</span>
    </div>
    <div class="top-right-meta">Agricultural Crop Windows</div>
  </div>

  <div class="section-title">
    <span>SEASONAL HARVEST CALENDAR | التقويم الموسمي للحصاد</span>
    <span class="badge-tag badge-emerald">Indicative Crop Windows</span>
  </div>
  <div class="notice-box" style="margin-bottom: 8px;">
    <strong>Official Crop Window Notice:</strong> "These are indicative Egyptian crop windows. Actual availability may vary by governorate, variety, weather conditions and farming schedule."<br>
    <span class="arabic">"الفترات التالية استرشادية للمحاصيل المصرية، وقد تختلف مواعيد التوافر الفعلية وفقاً للمحافظة والصنف والظروف الجوية والبرنامج الزراعي."</span>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
    <!-- Winter Table -->
    <div>
      <h3 style="font-size: 8.8pt; color: #0284c7; margin-bottom: 4px;">Winter Crops (المحاصيل الشتوية)</h3>
      <table class="corp-table">
        <thead>
          <tr>
            <th style="width: 58%;">Crop Name (EN / AR)</th>
            <th style="width: 42%;">Indicative Peak Season</th>
          </tr>
        </thead>
        <tbody>
          <tr><td><strong>Strawberries</strong><br><span class="arabic">الفراولة</span></td><td><span class="pill-month">December – April</span></td></tr>
          <tr><td><strong>Green peas</strong><br><span class="arabic">بسلة خضراء</span></td><td><span class="pill-month">November – March</span></td></tr>
          <tr><td><strong>Carrots</strong><br><span class="arabic">جزر</span></td><td><span class="pill-month">November – March</span></td></tr>
          <tr><td><strong>Broccoli</strong><br><span class="arabic">البروكلي</span></td><td><span class="pill-month">October – March</span></td></tr>
          <tr><td><strong>Cauliflower</strong><br><span class="arabic">القرنبيط</span></td><td><span class="pill-month">October – March</span></td></tr>
          <tr><td><strong>Artichokes</strong><br><span class="arabic">الخرشوف</span></td><td><span class="pill-month">October – March</span></td></tr>
          <tr><td><strong>Broad beans (Fava beans)</strong><br><span class="arabic">الفول الأخضر</span></td><td><span class="pill-month">November – April</span></td></tr>
          <tr><td><strong>Spinach</strong><br><span class="arabic">السبانخ</span></td><td><span class="pill-month">November – March</span></td></tr>
          <tr><td><strong>Taro</strong><br><span class="arabic">القلقاس</span></td><td><span class="pill-month">October – March</span></td></tr>
          <tr><td><strong>Green onions</strong><br><span class="arabic">بصل أخضر</span></td><td><span class="pill-month">November – May</span></td></tr>
          <tr><td><strong>Onions</strong><br><span class="arabic">بصل</span></td><td><span class="pill-month">November – May</span></td></tr>
        </tbody>
      </table>
    </div>

    <!-- Summer Table -->
    <div>
      <h3 style="font-size: 8.8pt; color: #d97706; margin-bottom: 4px;">Summer Crops (المحاصيل الصيفية)</h3>
      <table class="corp-table">
        <thead>
          <tr>
            <th style="width: 58%;">Crop Name (EN / AR)</th>
            <th style="width: 42%;">Indicative Peak Season</th>
          </tr>
        </thead>
        <tbody>
          <tr><td><strong>Molokhia (Jew’s Mallow)</strong><br><span class="arabic">الملوخية</span></td><td><span class="pill-month">May – September</span></td></tr>
          <tr><td><strong>Sweet corn</strong><br><span class="arabic">الذرة الحلوة</span></td><td><span class="pill-month">May – September</span></td></tr>
          <tr><td><strong>Sweet peppers</strong><br><span class="arabic">فلفل ألوان</span></td><td><span class="pill-month">June – October</span></td></tr>
          <tr><td><strong>Apricot</strong><br><span class="arabic">المشمش</span></td><td><span class="pill-month">May – July</span></td></tr>
          <tr><td><strong>Figs</strong><br><span class="arabic">التين</span></td><td><span class="pill-month">July – October</span></td></tr>
          <tr><td><strong>Mango (Keitt, Kent, Yasmina)</strong><br><span class="arabic">المانجو</span></td><td><span class="pill-month">July – October</span></td></tr>
          <tr><td><strong>Okra (Bamia)</strong><br><span class="arabic">البامية</span></td><td><span class="pill-month">April – October</span></td></tr>
          <tr><td><strong>Green beans</strong><br><span class="arabic">الفاصوليا الخضراء</span></td><td><span class="pill-month">Apr–Jul & Oct–Jan</span></td></tr>
          <tr><td><strong>Pomegranate arils</strong><br><span class="arabic">حبوب الرمان</span></td><td><span class="pill-month">September – December</span></td></tr>
          <tr><td><strong>Pumpkin</strong><br><span class="arabic">قرع عسل</span></td><td><span class="pill-month">August – January</span></td></tr>
          <tr><td><strong>Sweet potatoes</strong><br><span class="arabic">بطاطا حلوة</span></td><td><span class="pill-month">August – February</span></td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div style="background: #fffbeb; border: 1.5px solid #fde68a; border-radius: 5px; padding: 10px; margin-top: 8px;">
    <div style="font-weight: 800; font-size: 8.2pt; color: #92400e; margin-bottom: 3px;">
      Year-Round / Processed Items (منتجات مصنعة ومتاحة على مدار العام)
    </div>
    <p style="font-size: 7.4pt; color: #78350f; margin: 0 0 4px 0;">
      French fries and falafel may be produced or supplied throughout the year, subject to raw-material sourcing, production planning and customer demand.
    </p>
    <p class="arabic" style="font-size: 7.4pt; color: #78350f; margin: 0;">
      البطاطس نصف المقلية والفلافل: متاحة على مدار العام وفقاً لتوافر الخامات وخطة الإنتاج واحتياجات العملاء.
    </p>
  </div>
</div>

<!-- ========================================================= -->
<!-- PAGE 7: QUALITY & FOOD SAFETY STANDARDS (ENGLISH)           -->
<!-- ========================================================= -->
<div class="doc-page">
  <div class="page-top-bar">
    <div class="top-left-brand">
      <img src="{logo_b64}" class="top-logo-img" alt="logo">
      <span class="top-brand-text">GREEN ALEX</span>
    </div>
    <div class="top-right-meta">Quality & Food Safety Standards</div>
  </div>

  <div class="section-title">
    <span>QUALITY & FOOD SAFETY STANDARDS</span>
    <span class="badge-tag badge-emerald">EOS & Codex Benchmark</span>
  </div>
  <p class="section-subtitle">
    Key Egyptian and internationally recognised references relevant to frozen fruits and vegetables. The applicable edition, mandatory status, product scope and destination-market requirements must be verified before each product is released or exported.
  </p>

  <h3 style="font-size: 8.8pt; color: #064e3b; margin-bottom: 4px;">Egyptian Standards — EOS (الهيئة المصرية العامة للمواصفات والجودة)</h3>
  <table class="corp-table">
    <thead>
      <tr>
        <th style="width: 22%;">Standard No.</th>
        <th style="width: 38%;">Subject Title</th>
        <th style="width: 40%;">Official Catalogue Note</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>ES 2368 / 2021</strong></td><td>Quick Frozen Strawberries</td><td>EOS catalogue lists this as obligatory.</td></tr>
      <tr><td><strong>ES 1676 / 2005</strong></td><td>Frozen Mixed Vegetables</td><td>EOS catalogue lists this as obligatory; status shown as total modification.</td></tr>
      <tr><td><strong>ES 1681 / 2005</strong></td><td>Frozen Jew’s Mallow (Molokhia)</td><td>Listed in EOS catalogue; verify current text and status.</td></tr>
      <tr><td><strong>ES 1702 / 2005</strong></td><td>Frozen Okra</td><td>EOS catalogue lists this as obligatory; status shown as total modification.</td></tr>
      <tr><td><strong>ES 1743 / 2014</strong></td><td>Frozen Green Beans</td><td>EOS catalogue lists this as obligatory; status shown as updated.</td></tr>
      <tr><td><strong>ES 1746 / 2005</strong></td><td>Frozen Artichoke</td><td>Listed in EOS catalogue; verify current text and status.</td></tr>
      <tr><td><strong>ES 1748 / 2014</strong></td><td>Quick Frozen Peas</td><td>EOS catalogue lists this as obligatory; verify current edition/status.</td></tr>
      <tr><td><strong>ES 1749 / 2014</strong></td><td>Frozen Green Spinach</td><td>EOS catalogue lists this as obligatory; verify current edition/status.</td></tr>
      <tr><td><strong>ES 991 / 2008</strong></td><td>Methods of Analysis and Testing of Frozen Vegetables</td><td>EOS catalogue describes this as a non-obligatory testing-method standard.</td></tr>
    </tbody>
  </table>

  <h3 style="font-size: 8.8pt; color: #064e3b; margin: 8px 0 4px 0;">International Codex, ISO & GFSI References</h3>
  <table class="corp-table">
    <thead>
      <tr>
        <th style="width: 25%;">Reference Code</th>
        <th style="width: 35%;">Standard Title</th>
        <th style="width: 40%;">Scope & Relevance</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>Codex CXS 320-2015</strong></td><td>Standard for Quick-Frozen Vegetables</td><td>Product definition, quality factors, defects, contaminants, labelling.</td></tr>
      <tr><td><strong>Codex CXC 8-1976</strong></td><td>Code of Practice for Quick-Frozen Foods</td><td>Good handling practices, cryogenic freezing, cold storage at -18°C.</td></tr>
      <tr><td><strong>Codex CXS 1-1985</strong></td><td>Labelling of Prepackaged Foods</td><td>Mandatory declarations, lot identification, expiry & origin labelling.</td></tr>
      <tr><td><strong>Codex CXS 193-1995</strong></td><td>Contaminants and Toxins in Food</td><td>Statutory limits for heavy metals, nitrates, and toxic residues.</td></tr>
      <tr><td><strong>Codex Pesticide MRLs</strong></td><td>Maximum Residue Limits for Pesticides</td><td>Verified per commodity and importing country regulations (EU/FDA).</td></tr>
      <tr><td><strong>ISO 22000:2018 / HACCP</strong></td><td>Food Safety Management Systems</td><td>Hazard analysis, critical control points, allergen & recall protocols.</td></tr>
      <tr><td><strong>BRCGS / IFS Food</strong></td><td>GFSI Global Standards for Food Safety</td><td>Retailer-driven technical certification schemes where required.</td></tr>
    </tbody>
  </table>
</div>

<!-- ========================================================= -->
<!-- PAGE 8: QUALITY STANDARDS (ARABIC) & CORE QC POINTS         -->
<!-- ========================================================= -->
<div class="doc-page">
  <div class="page-top-bar">
    <div class="top-left-brand">
      <img src="{logo_b64}" class="top-logo-img" alt="logo">
      <span class="top-brand-text">GREEN ALEX</span>
    </div>
    <div class="top-right-meta">المواصفات القياسية ونقاط الجودة</div>
  </div>

  <div class="section-title arabic">
    <span>المواصفات الغذائية للجودة وسلامة الغذاء</span>
    <span class="badge-tag badge-emerald">مواصفات قياسية معتمدة</span>
  </div>
  <p class="section-subtitle arabic">
    يتضمن هذا القسم أهم المراجع المصرية والدولية ذات الصلة بمنتجات الفواكه والخضروات المجمدة. يجب مراجعة أحدث إصدار وحالة الإلزام ونطاق التطبيق ومتطلبات بلد الاستيراد قبل اعتماد مواصفة كل منتج أو تصديره.
  </p>

  <h3 class="arabic" style="font-size: 8.8pt; color: #064e3b; margin-bottom: 4px;">أولاً: المواصفات المصرية – الهيئة المصرية العامة للمواصفات والجودة (EOS)</h3>
  <table class="corp-table arabic-table">
    <thead>
      <tr>
        <th style="width: 25%;">رقم المواصفة</th>
        <th style="width: 35%;">موضوع المواصفة</th>
        <th style="width: 40%;">حالة المواصفة بالموقع الرسمي</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>م.ق.م 2368 / 2021</strong></td><td>الفراولة سريعة التجميد</td><td>مدرجة كمواصفة إلزامية.</td></tr>
      <tr><td><strong>م.ق.م 1676 / 2005</strong></td><td>الخضروات المشكلة المجمدة</td><td>مدرجة كمواصفة إلزامية؛ وحالتها تعديل كلي.</td></tr>
      <tr><td><strong>م.ق.م 1681 / 2005</strong></td><td>الملوخية المجمدة</td><td>مدرجة بدليل المواصفات؛ يرجى مراجعة النص المحدث.</td></tr>
      <tr><td><strong>م.ق.م 1702 / 2005</strong></td><td>البامية المجمدة</td><td>مدرجة كمواصفة إلزامية؛ وحالتها تعديل كلي.</td></tr>
      <tr><td><strong>م.ق.م 1743 / 2014</strong></td><td>الفاصوليا الخضراء المجمدة</td><td>مدرجة كمواصفة إلزامية؛ وحالتها محدثة.</td></tr>
      <tr><td><strong>م.ق.م 1746 / 2005</strong></td><td>الخرشوف المجمد</td><td>مدرجة بدليل المواصفات الرسمية.</td></tr>
      <tr><td><strong>م.ق.م 1748 / 2014</strong></td><td>البسلة سريعة التجميد</td><td>مدرجة كمواصفة إلزامية.</td></tr>
      <tr><td><strong>م.ق.م 1749 / 2014</strong></td><td>السبانخ الخضراء المجمدة</td><td>مدرجة كمواصفة إلزامية.</td></tr>
    </tbody>
  </table>

  <h3 class="arabic" style="font-size: 8.8pt; color: #064e3b; margin: 8px 0 4px 0;">ثانياً: نقاط الفحص والرقابة الأساسية لجودة منتجات IQF</h3>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 6px 8px;">
      <strong style="color: #064e3b; font-size: 7.4pt;">1. فحص الخامات الواردة:</strong>
      <p style="font-size: 7pt; color: #475569; margin: 2px 0 0 0;">مزارع معتمدة، درجة النضج، الطزاجة، التتبع وفحص الاستلام.</p>
    </div>
    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 6px 8px;">
      <strong style="color: #064e3b; font-size: 7.4pt;">2. التجهيز والتقطيع:</strong>
      <p style="font-size: 7pt; color: #475569; margin: 2px 0 0 0;">الغسيل، الفرز، التقشير، والتقطيع طبقاً للمواصفة المعتمدة للعميل.</p>
    </div>
    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 6px 8px;">
      <strong style="color: #064e3b; font-size: 7.4pt;">3. السلق وتعطيل الإنزيمات:</strong>
      <p style="font-size: 7pt; color: #475569; margin: 2px 0 0 0;">سلق محكوم معملياً وفق طبيعة كل صنف للحفاظ على اللون والنسيج.</p>
    </div>
    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 6px 8px;">
      <strong style="color: #064e3b; font-size: 7.4pt;">4. التجميد السريع IQF:</strong>
      <p style="font-size: 7pt; color: #475569; margin: 2px 0 0 0;">تجميد فردي فائق السرعة، والتحقق من وصول قلب المنتج إلى ‎-18°م.</p>
    </div>
    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 6px 8px;">
      <strong style="color: #064e3b; font-size: 7.4pt;">5. فحص المنتج النهائي:</strong>
      <p style="font-size: 7pt; color: #475569; margin: 2px 0 0 0;">اللون، الطعم، القوام، تجانس المقاس، خلو العيوب، وسلامة العبوة.</p>
    </div>
    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 6px 8px;">
      <strong style="color: #064e3b; font-size: 7.4pt;">6. سلامة الغذاء والتتبع:</strong>
      <p style="font-size: 7pt; color: #475569; margin: 2px 0 0 0;">كود التشغيلة، مطابقة المبيدات والملوثات، والتحكم الحراري لسلسلة التبريد.</p>
    </div>
  </div>
</div>

<!-- ========================================================= -->
<!-- PAGE 9: PRODUCT PHOTO GALLERY (PART 1: ITEMS 1 TO 12)       -->
<!-- ========================================================= -->
<div class="doc-page">
  <div class="page-top-bar">
    <div class="top-left-brand">
      <img src="{logo_b64}" class="top-logo-img" alt="logo">
      <span class="top-brand-text">GREEN ALEX</span>
    </div>
    <div class="top-right-meta">Visual Gallery — Part 1 (Items 1 to 12)</div>
  </div>

  <div class="section-title">
    <span>PRODUCT PHOTO GALLERY — PART 1</span>
    <span class="badge-tag badge-emerald">Authentic Factory Photos</span>
  </div>
  <p class="section-subtitle">
    High-resolution authentic imagery showing raw materials, cryogenic IQF freezing stages, and commercial export cuts.
  </p>

  <div class="gallery-grid">
    <!-- 1. Strawberry -->
    <div class="prod-card">
      <img src="{prod_imgs['strawberry']}" class="prod-card-img" alt="Strawberry">
      <div class="prod-card-body">
        <div class="prod-name-en">Strawberry</div>
        <div class="prod-name-ar">فراولة مجمدة</div>
        <div class="prod-styles-tag">Whole, halves, slices, diced</div>
      </div>
    </div>
    <!-- 2. Mango -->
    <div class="prod-card">
      <img src="{prod_imgs['mango']}" class="prod-card-img" alt="Mango">
      <div class="prod-card-body">
        <div class="prod-name-en">Mango (Keitt, Kent)</div>
        <div class="prod-name-ar">مانجو مكعبات وشرائح</div>
        <div class="prod-styles-tag">Diced, chunks, slices</div>
      </div>
    </div>
    <!-- 3. Pomegranate -->
    <div class="prod-card">
      <img src="{prod_imgs['pomegranate']}" class="prod-card-img" alt="Pomegranate">
      <div class="prod-card-body">
        <div class="prod-name-en">Pomegranate arils</div>
        <div class="prod-name-ar">حبوب رمان منقاة</div>
        <div class="prod-styles-tag">Cleaned whole arils</div>
      </div>
    </div>
    <!-- 4. Figs -->
    <div class="prod-card">
      <img src="{prod_imgs['figs']}" class="prod-card-img" alt="Figs">
      <div class="prod-card-body">
        <div class="prod-name-en">Figs</div>
        <div class="prod-name-ar">تين مجمد</div>
        <div class="prod-styles-tag">Whole, halves, diced</div>
      </div>
    </div>
    <!-- 5. Apricot -->
    <div class="prod-card">
      <img src="{prod_imgs['apricot']}" class="prod-card-img" alt="Apricot">
      <div class="prod-card-body">
        <div class="prod-name-en">Apricot</div>
        <div class="prod-name-ar">مشمش أنصاف ومكعبات</div>
        <div class="prod-styles-tag">Halves, quarters, diced</div>
      </div>
    </div>
    <!-- 6. Green peas -->
    <div class="prod-card">
      <img src="{prod_imgs['green-peas']}" class="prod-card-img" alt="Green peas">
      <div class="prod-card-body">
        <div class="prod-name-en">Green peas</div>
        <div class="prod-name-ar">بسلة خضراء</div>
        <div class="prod-styles-tag">Whole kernels</div>
      </div>
    </div>
    <!-- 7. Green beans -->
    <div class="prod-card">
      <img src="{prod_imgs['green-beans']}" class="prod-card-img" alt="Green beans">
      <div class="prod-card-body">
        <div class="prod-name-en">Green beans</div>
        <div class="prod-name-ar">فاصوليا خضراء</div>
        <div class="prod-styles-tag">Whole, cut</div>
      </div>
    </div>
    <!-- 8. Okra -->
    <div class="prod-card">
      <img src="{prod_imgs['okra']}" class="prod-card-img" alt="Okra">
      <div class="prod-card-body">
        <div class="prod-name-en">Okra (Bamia)</div>
        <div class="prod-name-ar">بامية درجات</div>
        <div class="prod-styles-tag">Extra, zero, one, two</div>
      </div>
    </div>
    <!-- 9. Broccoli -->
    <div class="prod-card">
      <img src="{prod_imgs['broccoli']}" class="prod-card-img" alt="Broccoli">
      <div class="prod-card-body">
        <div class="prod-name-en">Broccoli</div>
        <div class="prod-name-ar">بروكلي زهرات</div>
        <div class="prod-styles-tag">Florets (20–60 mm)</div>
      </div>
    </div>
    <!-- 10. Cauliflower -->
    <div class="prod-card">
      <img src="{prod_imgs['cauliflower']}" class="prod-card-img" alt="Cauliflower">
      <div class="prod-card-body">
        <div class="prod-name-en">Cauliflower</div>
        <div class="prod-name-ar">قرنبيط زهرات</div>
        <div class="prod-styles-tag">Florets (20–60 mm)</div>
      </div>
    </div>
    <!-- 11. Artichoke -->
    <div class="prod-card">
      <img src="{prod_imgs['artichoke']}" class="prod-card-img" alt="Artichoke">
      <div class="prod-card-body">
        <div class="prod-name-en">Artichoke</div>
        <div class="prod-name-ar">خرشوف قيعان وقلوب</div>
        <div class="prod-styles-tag">Hearts, bottoms, quarters</div>
      </div>
    </div>
    <!-- 12. Broad beans -->
    <div class="prod-card">
      <img src="{prod_imgs['broad-beans']}" class="prod-card-img" alt="Broad beans">
      <div class="prod-card-body">
        <div class="prod-name-en">Broad beans (Foul)</div>
        <div class="prod-name-ar">فول أخضر</div>
        <div class="prod-styles-tag">Peeled, unpeeled</div>
      </div>
    </div>
  </div>
</div>

<!-- ========================================================= -->
<!-- PAGE 10: PRODUCT PHOTO GALLERY (PART 2: ITEMS 13 TO 26)     -->
<!-- ========================================================= -->
<div class="doc-page">
  <div class="page-top-bar">
    <div class="top-left-brand">
      <img src="{logo_b64}" class="top-logo-img" alt="logo">
      <span class="top-brand-text">GREEN ALEX</span>
    </div>
    <div class="top-right-meta">Visual Gallery — Part 2 (Items 13 to 26)</div>
  </div>

  <div class="section-title">
    <span>PRODUCT PHOTO GALLERY — PART 2</span>
    <span class="badge-tag badge-gold">Vegetables & Processed</span>
  </div>

  <div class="gallery-grid" style="grid-template-columns: repeat(4, 1fr); gap: 7px;">
    <!-- 13. Spinach -->
    <div class="prod-card">
      <img src="{prod_imgs['spinach']}" class="prod-card-img" style="height: 80px;" alt="Spinach">
      <div class="prod-card-body">
        <div class="prod-name-en">Spinach</div>
        <div class="prod-name-ar">سبانخ مفرومة</div>
        <div class="prod-styles-tag">Leaf, cut, minced</div>
      </div>
    </div>
    <!-- 14. Molokhia -->
    <div class="prod-card">
      <img src="{prod_imgs['molokhia']}" class="prod-card-img" style="height: 80px;" alt="Molokhia">
      <div class="prod-card-body">
        <div class="prod-name-en">Molokhia</div>
        <div class="prod-name-ar">ملوخية خضراء</div>
        <div class="prod-styles-tag">Minced, chopped, leaf</div>
      </div>
    </div>
    <!-- 15. Sweet corn -->
    <div class="prod-card">
      <img src="{prod_imgs['sweet-corn']}" class="prod-card-img" style="height: 80px;" alt="Sweet corn">
      <div class="prod-card-body">
        <div class="prod-name-en">Sweet corn</div>
        <div class="prod-name-ar">ذرة حلوة وكيزان</div>
        <div class="prod-styles-tag">Kernels, half/whole cob</div>
      </div>
    </div>
    <!-- 16. Sweet peppers -->
    <div class="prod-card">
      <img src="{prod_imgs['sweet-peppers']}" class="prod-card-img" style="height: 80px;" alt="Sweet peppers">
      <div class="prod-card-body">
        <div class="prod-name-en">Sweet peppers</div>
        <div class="prod-name-ar">فلفل ألوان شرائح</div>
        <div class="prod-styles-tag">Strips, diced (tricolor)</div>
      </div>
    </div>
    <!-- 17. Green onions -->
    <div class="prod-card">
      <img src="{prod_imgs['green-onions']}" class="prod-card-img" style="height: 80px;" alt="Green onions">
      <div class="prod-card-body">
        <div class="prod-name-en">Green onion & onion</div>
        <div class="prod-name-ar">بصل وبصل أخضر</div>
        <div class="prod-styles-tag">Whole, cut, rings, diced</div>
      </div>
    </div>
    <!-- 18. Taro -->
    <div class="prod-card">
      <img src="{prod_imgs['taro']}" class="prod-card-img" style="height: 80px;" alt="Taro">
      <div class="prod-card-body">
        <div class="prod-name-en">Taro</div>
        <div class="prod-name-ar">قلقاس مكعبات</div>
        <div class="prod-styles-tag">Diced cubes</div>
      </div>
    </div>
    <!-- 19. Pumpkin -->
    <div class="prod-card">
      <img src="{prod_imgs['pumpkin']}" class="prod-card-img" style="height: 80px;" alt="Pumpkin">
      <div class="prod-card-body">
        <div class="prod-name-en">Pumpkin</div>
        <div class="prod-name-ar">قرع عسل مكعبات</div>
        <div class="prod-styles-tag">Diced cubes</div>
      </div>
    </div>
    <!-- 20. Sweet potatoes -->
    <div class="prod-card">
      <img src="{prod_imgs['sweet-potatoes']}" class="prod-card-img" style="height: 80px;" alt="Sweet potatoes">
      <div class="prod-card-body">
        <div class="prod-name-en">Sweet potatoes</div>
        <div class="prod-name-ar">بطاطا حلوة مكعبات</div>
        <div class="prod-styles-tag">Diced, sliced, strips</div>
      </div>
    </div>
    <!-- 21. Mixed peas & carrots -->
    <div class="prod-card">
      <img src="{prod_imgs['mixed-peas-carrots']}" class="prod-card-img" style="height: 80px;" alt="Peas & carrots">
      <div class="prod-card-body">
        <div class="prod-name-en">Mixed peas & carrots</div>
        <div class="prod-name-ar">بسلة وجزر مكعبات</div>
        <div class="prod-styles-tag">Whole peas & diced carrots</div>
      </div>
    </div>
    <!-- 22. Mixed 3-way -->
    <div class="prod-card">
      <img src="{prod_imgs['mixed-3way']}" class="prod-card-img" style="height: 80px;" alt="Mixed 3-way">
      <div class="prod-card-body">
        <div class="prod-name-en">Mixed 3-way</div>
        <div class="prod-name-ar">خضار مشكل ثلاثي</div>
        <div class="prod-styles-tag">Peas, carrots, green beans</div>
      </div>
    </div>
    <!-- 23. Mixed 4-way -->
    <div class="prod-card">
      <img src="{prod_imgs['mixed-4way']}" class="prod-card-img" style="height: 80px;" alt="Mixed 4-way">
      <div class="prod-card-body">
        <div class="prod-name-en">Mixed 4-way</div>
        <div class="prod-name-ar">خضار مشكل رباعي</div>
        <div class="prod-styles-tag">Peas, carrots, beans, corn</div>
      </div>
    </div>
    <!-- 24. Custom blends -->
    <div class="prod-card">
      <img src="{prod_imgs['custom-blends']}" class="prod-card-img" style="height: 80px;" alt="Custom blends">
      <div class="prod-card-body">
        <div class="prod-name-en">Custom blends</div>
        <div class="prod-name-ar">خلطات خضار مخصصة</div>
        <div class="prod-styles-tag">To buyer custom formula</div>
      </div>
    </div>
    <!-- 25. French fries -->
    <div class="prod-card">
      <img src="{prod_imgs['french-fries']}" class="prod-card-img" style="height: 80px;" alt="French fries">
      <div class="prod-card-body">
        <div class="prod-name-en">French fries</div>
        <div class="prod-name-ar">بطاطس نصف مقلية</div>
        <div class="prod-styles-tag">Straight cut (Par-fried)</div>
      </div>
    </div>
    <!-- 26. Falafel -->
    <div class="prod-card">
      <img src="{prod_imgs['falafel']}" class="prod-card-img" style="height: 80px;" alt="Falafel">
      <div class="prod-card-body">
        <div class="prod-name-en">Falafel (Taameya)</div>
        <div class="prod-name-ar">فلافل / طعمية</div>
        <div class="prod-styles-tag">Balls (Plain / Sesame)</div>
      </div>
    </div>
  </div>
</div>

<!-- ========================================================= -->
<!-- PAGE 11: CONTACT & CORPORATE GOVERNANCE                     -->
<!-- ========================================================= -->
<div class="doc-page">
  <div class="page-top-bar">
    <div class="top-left-brand">
      <img src="{logo_b64}" class="top-logo-img" alt="logo">
      <span class="top-brand-text">GREEN ALEX</span>
    </div>
    <div class="top-right-meta">Export Desk & Commercial Inquiries</div>
  </div>

  <div style="text-align: center; margin-bottom: 16px;">
    <img src="{logo_b64}" style="width: 130px; height: auto; margin-bottom: 8px;" alt="GREEN ALEX LOGO">
    <h2 style="font-size: 16pt; color: #064e3b; margin-bottom: 2px;">CONTACT & EXPORT PROCUREMENT DESK</h2>
    <div style="font-size: 8.5pt; color: #d97706; font-weight: 700;">GREEN ALEX FOR AGRICULTURAL CROPS & FOOD PROCESSING</div>
    <div style="font-size: 7.8pt; color: #64748b;">Established 1999 • Founded & Managed by Dr. Mohamed Gabr</div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px;">
    <!-- English Info -->
    <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 6px; padding: 12px;">
      <h3 style="font-size: 9.5pt; color: #064e3b; margin-bottom: 6px;">Commercial Administration</h3>
      <div style="font-size: 7.8pt; line-height: 1.6; color: #334155;">
        <strong>Company:</strong> GREEN ALEX<br>
        <strong>Founder & Owner:</strong> Dr. Mohamed Gabr<br>
        <strong>Commercial Reg:</strong> Rashid, Beheira Governorate, Egypt<br>
        <strong>Administration Office:</strong> 10 Ibn Shogaa Street, Al-Azareeta, Alexandria, Egypt<br>
        <strong>Direct WhatsApp:</strong> +20 109 300 3736<br>
        <strong>Product Focus:</strong> IQF Fruits, Vegetables, and Processed Range
      </div>
    </div>

    <!-- Arabic Info -->
    <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 6px; padding: 12px; direction: rtl; text-align: right;">
      <h3 class="arabic" style="font-size: 9.5pt; color: #064e3b; margin-bottom: 6px;">بيانات التواصل والإدارة الرسمية</h3>
      <div class="arabic" style="font-size: 7.8pt; line-height: 1.6; color: #334155;">
        <strong>اسم الشركة:</strong> GREEN ALEX (جرين أليكس)<br>
        <strong>المؤسس والمالك:</strong> الدكتور/ محمد جبر<br>
        <strong>السجل التجاري:</strong> رشيد – محافظة البحيرة، جمهورية مصر العربية<br>
        <strong>مقر الإدارة:</strong> 10 شارع ابن شجاع، الأزاريطة، الإسكندرية، مصر<br>
        <strong>واتساب التصدير المباشر:</strong> 3736 300 109 20+<br>
        <strong>التوريد:</strong> فواكه وخضروات مجمدة IQF وعلامة Virdi Va™
      </div>
    </div>
  </div>

  <div style="border: 1px dashed #cbd5e1; border-radius: 6px; padding: 12px; background: #ffffff; margin-bottom: 16px;">
    <h4 style="font-size: 8.5pt; color: #064e3b; margin-bottom: 4px;">Commercial Procurement & RFQ Protocol</h4>
    <p style="font-size: 7.4pt; color: #475569; margin: 0 0 6px 0; line-height: 1.4;">
      Prospective international importers and institutional buyers are invited to submit export Requests for Quotation (RFQ) directly to the management desk. GREEN ALEX provides certified certificate of analysis (COA), phytosanitary inspection documents, container temperature logs, and custom labeling conforming to destination-market food regulations.
    </p>
    <div style="display: flex; justify-content: space-between; font-size: 7.2pt; color: #059669; font-weight: 700;">
      <span>✓ Official Product Specification Sheets</span>
      <span>✓ Pre-Shipment Container Inspection</span>
      <span>✓ CIF / FOB / CFR Port Delivery Terms</span>
    </div>
  </div>

  <div style="margin-top: auto; border-top: 1.5px solid #059669; padding-top: 10px; display: flex; justify-content: space-between; align-items: center; font-size: 7pt; color: #64748b;">
    <div>
      © 1999–2026 GREEN ALEX. All Rights Reserved.<br>
      Proprietary Technical Document for Authorized Commercial Distribution.
    </div>
    <div style="text-align: right;">
      <strong>Certified Sourcing Season:</strong> 2026 / 2027<br>
      <span class="arabic">شركة جرين أليكس للحاصلات الزراعية والتصنيع الغذائي</span>
    </div>
  </div>
</div>

</body>
</html>
"""

    html_path = os.path.abspath("portfolio_full.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"portfolio_full.html written successfully ({len(html)} bytes).")

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    output_pdf = os.path.abspath("GREEN_ALEX_IQF_Product_Portfolio_Updated.pdf")

    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf}",
        html_path
    ]

    print("Compiling Master PDF via Chrome Headless...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Return code:", res.returncode)
    if res.stderr:
        print("Stderr:", res.stderr[:300])

    if os.path.exists(output_pdf):
        size = os.path.getsize(output_pdf)
        print(f"SUCCESS: PDF created at {output_pdf} ({size} bytes)")
        reader = PdfReader(output_pdf)
        print(f"Total Pages in Master PDF: {len(reader.pages)}")

        # Also copy to GREEN_ALEX_IQF_Product_Portfolio.pdf if possible
        import shutil
        target_name = os.path.abspath("GREEN_ALEX_IQF_Product_Portfolio.pdf")
        try:
            shutil.copyfile(output_pdf, target_name)
            print("Also updated GREEN_ALEX_IQF_Product_Portfolio.pdf successfully.")
        except Exception as e:
            print("Note: GREEN_ALEX_IQF_Product_Portfolio.pdf is open in an external viewer, master copy is GREEN_ALEX_IQF_Product_Portfolio_Updated.pdf")

if __name__ == '__main__':
    generate_master_pdf()

