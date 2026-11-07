import os
import subprocess
import base64
from pypdf import PdfReader

def generate_pdf():
    # Read logo base64
    logo_path = 'assets/images/logo_clean.png'
    logo_b64 = ''
    if os.path.exists(logo_path):
        with open(logo_path, 'rb') as f:
            logo_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>GREEN ALEX — Website Portfolio Structure & Content Review</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  @page {{
    size: A4 portrait;
    margin: 10mm 12mm 10mm 12mm;
    @bottom-left {{
      content: "GREEN ALEX | Corporate Portfolio Structure Review";
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 7pt;
      color: #94a3b8;
    }}
    @bottom-right {{
      content: "Page " counter(page);
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 7pt;
      color: #94a3b8;
      font-weight: 600;
    }}
  }}

  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}

  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #1e293b;
    background: #ffffff;
    line-height: 1.38;
    font-size: 8.4pt;
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

  /* Colors */
  :root {{
    --navy-primary: #0a2540;
    --navy-dark: #061829;
    --navy-light: #1e3a5f;
    --emerald-primary: #0f766e;
    --emerald-dark: #115e59;
    --emerald-light: #f0fdf4;
    --emerald-border: #86efac;
    --gold-accent: #c59b27;
    --gold-light: #fef9c3;
    --slate-border: #cbd5e1;
    --slate-bg: #f8fafc;
    --slate-text: #475569;
  }}

  /* Header Bar in Document Pages */
  .doc-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #0f766e;
    padding-bottom: 4px;
    margin-bottom: 8px;
  }}
  .doc-header .brand {{
    font-size: 9pt;
    font-weight: 800;
    color: var(--navy-primary);
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .doc-header .doc-type {{
    font-size: 7.5pt;
    font-weight: 700;
    color: var(--emerald-dark);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  /* Typography */
  h1, h2, h3, h4 {{
    color: var(--navy-primary);
    margin-top: 0;
    font-weight: 700;
  }}
  h1 {{ font-size: 17pt; line-height: 1.2; }}
  h2 {{ 
    font-size: 11pt; 
    border-bottom: 1.5px solid #cbd5e1; 
    padding-bottom: 3px; 
    margin-bottom: 6px;
    margin-top: 8px;
    color: var(--navy-primary);
  }}
  h3 {{ 
    font-size: 9.2pt; 
    margin-top: 7px; 
    margin-bottom: 3px; 
    color: var(--emerald-dark); 
    font-weight: 700;
  }}
  h4 {{
    font-size: 8.4pt;
    margin-top: 5px;
    margin-bottom: 2px;
    color: #334155;
  }}
  p {{
    margin: 0 0 6px 0;
  }}

  /* Cover Page */
  .cover-card {{
    height: 270mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 26px 22px;
    border: 2px solid #e2e8f0;
    background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
    border-radius: 6px;
    box-sizing: border-box;
  }}
  .cover-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .cover-logo {{
    max-height: 75px;
    object-fit: contain;
  }}
  .cover-badge {{
    background: var(--navy-primary);
    color: #ffffff;
    padding: 4px 10px;
    border-radius: 14px;
    font-size: 7.2pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
  }}
  .cover-hero {{
    margin: 15px 0;
  }}
  .cover-pill {{
    display: inline-block;
    background: #ecfdf5;
    color: var(--emerald-dark);
    border: 1px solid #a7f3d0;
    padding: 2.5px 8px;
    border-radius: 8px;
    font-size: 7.8pt;
    font-weight: 700;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .cover-title {{
    font-size: 24pt;
    font-weight: 800;
    color: var(--navy-primary);
    line-height: 1.1;
    margin-bottom: 5px;
    letter-spacing: -0.5px;
  }}
  .cover-title-sub {{
    font-size: 13pt;
    font-weight: 700;
    color: #0f766e;
    margin-bottom: 10px;
  }}
  .cover-desc {{
    font-size: 9pt;
    font-weight: 400;
    color: var(--slate-text);
    margin-bottom: 16px;
    line-height: 1.45;
  }}
  .cover-meta-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-left: 4px solid var(--emerald-primary);
    border-radius: 4px;
    padding: 12px;
  }}
  .cover-meta-item .label {{
    color: #64748b;
    font-size: 7.2pt;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 1px;
  }}
  .cover-meta-item .val {{
    color: var(--navy-primary);
    font-weight: 700;
    font-size: 8.5pt;
  }}
  .cover-footer {{
    border-top: 1px solid #e2e8f0;
    padding-top: 10px;
    display: flex;
    justify-content: space-between;
    font-size: 7.2pt;
    color: #64748b;
    font-weight: 600;
  }}

  /* Tables */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 6px;
    font-size: 7.6pt;
  }}
  th, td {{
    padding: 3.5px 6px;
    text-align: left;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: middle;
  }}
  th {{
    background-color: #f1f5f9;
    color: var(--navy-primary);
    font-weight: 700;
    font-size: 7.3pt;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    border-top: 1px solid #cbd5e1;
    border-bottom: 1.5px solid #0f766e;
  }}
  tr:nth-child(even) td {{
    background-color: #f8fafc;
  }}

  /* Callout & Cards */
  .callout {{
    border-radius: 4px;
    padding: 6px 9px;
    margin-bottom: 6px;
    font-size: 7.8pt;
    line-height: 1.4;
  }}
  .callout.emerald {{
    background-color: #f0fdf4;
    border-left: 3.5px solid #0f766e;
    color: #064e3b;
  }}
  .callout.gold {{
    background-color: #fffbeb;
    border-left: 3.5px solid #d97706;
    color: #78350f;
  }}
  .info-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 7px 10px;
    margin-bottom: 6px;
  }}
  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
  }}
  .page-spec-header {{
    background: #0a2540;
    color: #ffffff;
    padding: 4px 10px;
    border-radius: 3px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 6px;
  }}
  .page-spec-header .page-title {{
    font-size: 9pt;
    font-weight: 800;
    letter-spacing: 0.5px;
  }}
  .page-spec-header .page-id {{
    background: #0f766e;
    padding: 2px 7px;
    border-radius: 10px;
    font-size: 6.8pt;
    font-weight: 700;
    letter-spacing: 0.5px;
  }}

  /* Badges */
  .badge {{
    display: inline-block;
    padding: 1.5px 5px;
    border-radius: 3px;
    font-size: 6.8pt;
    font-weight: 700;
    text-transform: uppercase;
  }}
  .badge-obligatory {{ background: #fee2e2; color: #991b1b; }}
  .badge-verify {{ background: #fef3c7; color: #92400e; }}
  .badge-updated {{ background: #dbeafe; color: #1e40af; }}
  .badge-standard {{ background: #e2e8f0; color: #475569; }}
  .badge-new {{ background: #d1fae5; color: #065f46; font-weight: 800; border: 1px solid #34d399; }}

  .disclaimer-box {{
    background: #fff1f2;
    border: 1px solid #fecdd3;
    border-left: 3.5px solid #e11d48;
    border-radius: 4px;
    padding: 6px 9px;
    font-size: 7.5pt;
    color: #881337;
    margin-top: 5px;
    line-height: 1.35;
  }}
  .disclaimer-title {{
    font-weight: 800;
    text-transform: uppercase;
    font-size: 7.2pt;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
    display: flex;
    align-items: center;
    gap: 4px;
  }}

  .checkbox {{
    width: 11px;
    height: 11px;
    border: 1.2px solid #0f766e;
    border-radius: 2px;
    display: inline-block;
    vertical-align: middle;
    margin-right: 5px;
    background: #ffffff;
  }}
  .checklist-item {{
    display: flex;
    align-items: center;
    margin-bottom: 3.5px;
    font-size: 7.6pt;
  }}
</style>
</head>
<body>

  <!-- ================= PAGE 1: COVER PAGE ================= -->
  <div class="doc-page">
    <div class="cover-card">
      <div class="cover-top">
        <img src="{logo_b64}" alt="GREEN ALEX Logo" class="cover-logo">
        <div class="cover-badge">Client Proposal • Official Review</div>
      </div>

      <div class="cover-hero">
        <div class="cover-pill">Website Portfolio Structure & Content Review Document</div>
        <div class="cover-title">GREEN ALEX</div>
        <div class="cover-title-sub">IQF PRODUCTS PORTFOLIO & B2B WEBSITE ARCHITECTURE</div>
        <div class="cover-desc">
          A comprehensive structural proposal and technical content audit for the new international corporate web portfolio of <strong>GREEN ALEX</strong> (Founded in 1999 by <strong>Dr. Mohamed Gabr</strong>). Designed to showcase the complete 26-product export catalogue, seasonal harvest calendar, and certified food safety standards for overseas buyers.
        </div>

        <div class="cover-meta-grid">
          <div class="cover-meta-item">
            <div class="label">Client Company</div>
            <div class="val">GREEN ALEX (شركة جرين أليكس للحاصلات الزراعية)</div>
          </div>
          <div class="cover-meta-item">
            <div class="label">Founder & Owner</div>
            <div class="val">Dr. Mohamed Gabr (الدكتور / محمد جبر)</div>
          </div>
          <div class="cover-meta-item">
            <div class="label">Document Scope</div>
            <div class="val">Website Architecture, Content Map & Product Audit</div>
          </div>
          <div class="cover-meta-item">
            <div class="label">Catalogue Scale</div>
            <div class="val">26 IQF Products (Fruits, Vegetables & Processed)</div>
          </div>
          <div class="cover-meta-item">
            <div class="label">Review Version</div>
            <div class="val">Version 2.0 (Updated with All Additional Products & Revisions)</div>
          </div>
          <div class="cover-meta-item">
            <div class="label">Direct Trade WhatsApp Desk</div>
            <div class="val">+20 109 300 3736 (01093003736)</div>
          </div>
        </div>
      </div>

      <div class="cover-footer">
        <div>Alexandria Administration: 10 Ibn Shogaa St., Al-Azareeta</div>
        <div>Commercial Registration: Rashid, Beheira Governorate, Egypt</div>
        <div>Confidential • For Client Review & Approval</div>
      </div>
    </div>
  </div>

  <!-- ================= PAGE 2: EXECUTIVE SUMMARY & 6-PAGE ARCHITECTURE ================= -->
  <div class="doc-page">
    <div class="doc-header">
      <div class="brand">GREEN ALEX | IQF PRODUCTS PORTFOLIO</div>
      <div class="doc-type">Executive Summary & Website Structure</div>
    </div>

    <h2>1. Executive Summary & Project Objectives</h2>
    <p>
      This document presents the strategic website architecture and content distribution proposed for <strong>GREEN ALEX</strong>. The primary objective is to build an authoritative, modern corporate digital presence tailored for international food buyers, supermarket procurement teams, and commercial importers.
    </p>

    <div class="grid-2">
      <div class="info-card">
        <h4>Company Identity & Corporate Background</h4>
        <p style="font-size: 7.8pt; margin: 0;">
          <strong>Company Name:</strong> GREEN ALEX (شركة جرين أليكس للحاصلات الزراعية)<br>
          <strong>Specialization:</strong> IQF fruits, IQF vegetables, and processed ready-to-cook items.<br>
          <strong>Established:</strong> 1999 (Over 27 years in Food Processing).<br>
          <strong>Founder / Owner:</strong> <strong>Dr. Mohamed Gabr</strong>.<br>
          <strong>Commercial Registration:</strong> Rashid, Beheira Governorate, Egypt.<br>
          <strong>Administration Office:</strong> 10 Ibn Shogaa Street, Al-Azareeta, Alexandria, Egypt.<br>
          <strong>Website Languages:</strong> Bilingual parity (English & Arabic).
        </p>
      </div>

      <div class="info-card">
        <h4>Website Purpose & Boundary Constraints</h4>
        <p style="font-size: 7.8pt; margin-bottom: 4px;">
          The agreed project scope is strictly a <strong>Corporate Portfolio Website</strong>. It is designed to establish international B2B credibility, showcase product capabilities, demonstrate adherence to strict food safety standards, and facilitate direct export inquiries.
        </p>
        <div class="callout gold" style="margin: 0; padding: 4px 7px; font-size: 7.4pt;">
          <strong>Strict Scope Boundaries:</strong><br>
          • NOT an e-commerce or cart-checkout platform.<br>
          • NOT an online transactional consumer shop.<br>
          • NOT an operational internal ERP or export freight portal.
        </div>
      </div>
    </div>

    <h2>2. Architectural Overview of the Proposed 6 Pages</h2>
    <p>
      All information provided by the client has been logically organized into a focused, user-friendly 6-page navigation hierarchy:
    </p>

    <table>
      <thead>
        <tr>
          <th style="width: 14%;">Page No. & Slug</th>
          <th style="width: 24%;">Page Title (EN / AR)</th>
          <th style="width: 37%;">Strategic Purpose</th>
          <th style="width: 25%;">Primary Target Audience</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>PAGE 01</strong><br><code>/home</code></td>
          <td><strong>Home</strong><br><span class="arabic">الرئيسية</span></td>
          <td>Executive brand overview, core value proposition, category teasers, harvest glimpse, and trust indicators.</td>
          <td>International buyers, food brokers, retail purchasers.</td>
        </tr>
        <tr>
          <td><strong>PAGE 02</strong><br><code>/about-us</code></td>
          <td><strong>About Us</strong><br><span class="arabic">نبذة عن الشركة</span></td>
          <td>Company heritage (Est. 1999), founder leadership (Dr. Mohamed Gabr), sourcing methodology, and customization policy.</td>
          <td>Procurement directors, commercial audit teams.</td>
        </tr>
        <tr>
          <td><strong>PAGE 03</strong><br><code>/products</code></td>
          <td><strong>Our Products</strong><br><span class="arabic">منتجاتنا</span></td>
          <td>Full technical catalogue of <strong>26 products</strong> across IQF Fruits (5), IQF Vegetables (15), and Mixed/Processed (6) with cutting sizes and grades.</td>
          <td>Food importers, supermarket buyers, industrial caterers.</td>
        </tr>
        <tr>
          <td><strong>PAGE 04</strong><br><code>/harvest-calendar</code></td>
          <td><strong>Seasonal Harvest Calendar</strong><br><span class="arabic">التقويم الموسمي للحصاد</span></td>
          <td>Indicative Egyptian crop windows (Winter, Summer, Year-round) to facilitate export planning and supply contracts.</td>
          <td>Supply chain planners, agricultural procurement leads.</td>
        </tr>
        <tr>
          <td><strong>PAGE 05</strong><br><code>/quality-safety</code></td>
          <td><strong>Quality & Food Safety</strong><br><span class="arabic">الجودة وسلامة الغذاء</span></td>
          <td>Egyptian EOS standards, international Codex/ISO references, 8-stage IQF QC pipeline, and legal compliance disclaimers.</td>
          <td>Quality assurance (QA) auditors, technical compliance officers.</td>
        </tr>
        <tr>
          <td><strong>PAGE 06</strong><br><code>/contact-us</code></td>
          <td><strong>Contact Us</strong><br><span class="arabic">اتصل بنا</span></td>
          <td>Headquarters address, official registration, interactive RFQ builder, and direct WhatsApp communication desk.</td>
          <td>Prospective buyers seeking quotes and spec sheets.</td>
        </tr>
      </tbody>
    </table>

    <div class="callout emerald">
      <strong>Client Alignment Summary:</strong> This 6-page structure provides foreign B2B buyers with complete operational transparency while keeping navigation intuitive, fast, and focused on commercial inquiries.
    </div>
  </div>

  <!-- ================= PAGE 3: PAGE 01 (HOME) & PAGE 02 (ABOUT US) ================= -->
  <div class="doc-page">
    <div class="doc-header">
      <div class="brand">GREEN ALEX | IQF PRODUCTS PORTFOLIO</div>
      <div class="doc-type">Page 01 & Page 02 Structure Specifications</div>
    </div>

    <div class="page-spec-header">
      <div class="page-title">PAGE 01 — HOME (الرئيسية)</div>
      <div class="page-id">Architecture Spec</div>
    </div>

    <p><strong>Primary Purpose:</strong> Introduce GREEN ALEX with an authoritative, modern corporate impression and provide visitors with a clear roadmap into the product portfolio, seasonal sourcing, and technical standards.</p>

    <div class="info-card" style="margin-bottom: 6px;">
      <h4>Exact Content Allocation & Structural Hierarchy:</h4>
      <ul style="margin: 0; padding-left: 18px; font-size: 7.8pt;">
        <li><strong>Brand Title:</strong> <code>GREEN ALEX</code> (شركة جرين أليكس للحاصلات الزراعية).</li>
        <li><strong>Main Hero Heading:</strong> <code>IQF PRODUCTS PORTFOLIO</code> (بورتفوليو منتجات التجميد السريع IQF).</li>
        <li><strong>Supporting Value Line:</strong> <code>Seasonal Harvest Calendar • Product Forms • Quality Standards</code>.</li>
        <li><strong>Corporate Highlights:</strong> Established 1999 • Founded by <strong>Dr. Mohamed Gabr</strong> • Rashid (Beheira) & Alexandria, Egypt.</li>
        <li><strong>Concise Company Introduction:</strong> Bilingual corporate profile based strictly on supplied company data.</li>
        <li><strong>Three Core Category Cards:</strong> 1. IQF Fruits (5 products), 2. IQF Vegetables (15 products), 3. Mixed & Processed (6 products) — Total 26 Products.</li>
        <li><strong>Seasonal Harvest Preview:</strong> Interactive teaser highlighting active Egyptian crop windows linking to Page 04.</li>
        <li><strong>Quality & Food Safety Badge:</strong> Highlighting EOS and international Codex/ISO compliance references linking to Page 05.</li>
        <li><strong>Direct WhatsApp CTA:</strong> Instant navigation to WhatsApp export desk (+201093003736).</li>
      </ul>
    </div>

    <div class="page-spec-header" style="margin-top: 8px;">
      <div class="page-title">PAGE 02 — ABOUT US (نبذة عن الشركة)</div>
      <div class="page-id">Architecture Spec</div>
    </div>

    <p><strong>Primary Purpose:</strong> Present the company’s history, executive leadership, operational approach, and tailoring capabilities to build solid B2B trust without unsupported claims.</p>

    <div class="grid-2">
      <div class="info-card">
        <h4>English Corporate Profile</h4>
        <p style="font-size: 7.7pt; margin: 0;">
          "GREEN ALEX is an Egyptian food-processing company established in 1999 and founded by <strong>Dr. Mohamed Gabr</strong>. The company focuses on the processing and supply of individually quick frozen (IQF) fruits and vegetables, alongside selected processed and ready-to-cook products.<br><br>
          With a seasonal raw-material approach, GREEN ALEX plans production around optimum crop availability and customer specifications. Product styles, grading, cutting sizes, blends and packing formats can be tailored subject to raw-material availability, approved specifications and production capability."
        </p>
      </div>
      <div class="info-card arabic">
        <h4 style="text-align: right;">نبذة عن الشركة باللغة العربية</h4>
        <p style="font-size: 7.7pt; margin: 0;">
          "شركة GREEN ALEX هي شركة مصرية تأسست عام 1999 على يد الدكتور/ محمد جبر، وتعمل في مجال تجهيز وتصنيع وتوريد منتجات الفواكه والخضروات المجمدة بالتجميد الفردي السريع (IQF)، إلى جانب بعض المنتجات المصنعة والجاهزة للطهي.<br><br>
          تعتمد الشركة على التخطيط الموسمي لتوافر المحاصيل الزراعية، مع إمكانية تقديم أشكال تصنيع ومقاسات تقطيع ودرجات فرز وخلطات وتعبئة مختلفة وفقاً لمتطلبات العملاء، وبما يتوافق مع توافر الخامات والمواصفات المعتمدة والطاقة الإنتاجية."
        </p>
      </div>
    </div>

    <table style="margin-top: 6px;">
      <thead>
        <tr>
          <th style="width: 35%;">Item / البيان</th>
          <th style="width: 65%;">Official Details / التفاصيل المعتمدة</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Company Name / اسم الشركة</strong></td>
          <td>GREEN ALEX (شركة جرين أليكس للحاصلات الزراعية)</td>
        </tr>
        <tr>
          <td><strong>Established / سنة التأسيس</strong></td>
          <td>1999</td>
        </tr>
        <tr>
          <td><strong>Founder & Owner / المؤسس والمالك</strong></td>
          <td><strong>Dr. Mohamed Gabr</strong> (الدكتور / محمد جبر)</td>
        </tr>
        <tr>
          <td><strong>Commercial Registration / السجل التجاري</strong></td>
          <td>Rashid, Beheira Governorate, Egypt (رشيد – محافظة البحيرة)</td>
        </tr>
        <tr>
          <td><strong>Administration Office / مقر الإدارة</strong></td>
          <td>10 Ibn Shogaa Street, Al-Azareeta, Alexandria, Egypt (10 شارع ابن شجاع، الأزاريطة، الإسكندرية)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ================= PAGE 4: PAGE 03 (OUR PRODUCTS) — PART 1 ================= -->
  <div class="doc-page">
    <div class="doc-header">
      <div class="brand">GREEN ALEX | IQF PRODUCTS PORTFOLIO</div>
      <div class="doc-type">Page 03 Product Catalogue (Part 1: Fruits & Vegetables)</div>
    </div>

    <div class="page-spec-header">
      <div class="page-title">PAGE 03 — OUR PRODUCTS (منتجاتنا) — PART 1</div>
      <div class="page-id">26-Product Portfolio Spec</div>
    </div>

    <p style="margin-bottom: 4px;"><strong>Primary Purpose:</strong> Complete technical catalogue reflecting all commercial styles, cutting dimensions, and client modifications across 26 export products.</p>

    <h3 style="color: var(--navy-primary); border-bottom: 1.5px solid #0f766e; padding-bottom: 2px; margin-top: 4px;">A. IQF FRUITS (الفواكه المجمدة) — 4 Products</h3>
    <table>
      <thead>
        <tr>
          <th style="width: 25%;">Product (EN / AR)</th>
          <th style="width: 35%;">Available Styles / أشكال التصنيع</th>
          <th style="width: 40%;">Typical Commercial Sizes / مقاسات التقطيع والفرز</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Mango</strong> | <span class="arabic">مانجو</span></td>
          <td>Diced, chunks, slices</td>
          <td>Customer specifications / مواصفات حسب العميل</td>
        </tr>
        <tr>
          <td><strong>Pomegranate arils</strong> | <span class="arabic">حبوب رمان</span></td>
          <td>Cleaned whole arils</td>
          <td>Customer specification</td>
        </tr>
        <tr>
          <td><strong>Figs</strong> | <span class="arabic">تين</span> <span class="badge badge-new">New</span></td>
          <td>Whole, halves, quarters, diced</td>
          <td>Customer specifications</td>
        </tr>
        <tr>
          <td><strong>Apricot</strong> | <span class="arabic">مشمش</span> <span class="badge badge-new">New</span></td>
          <td>Halves, quarters, diced</td>
          <td>Customer specifications</td>
        </tr>
      </tbody>
    </table>

    <h3 style="color: var(--navy-primary); border-bottom: 1.5px solid #0f766e; padding-bottom: 2px; margin-top: 6px;">B. IQF VEGETABLES (الخضروات المجمدة) — Part 1 (Items 1 to 8)</h3>
    <table>
      <thead>
        <tr>
          <th style="width: 25%;">Product (EN / AR)</th>
          <th style="width: 35%;">Available Styles / أشكال التصنيع</th>
          <th style="width: 40%;">Typical Commercial Sizes / مقاسات التقطيع والفرز</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Strawberry</strong> | <span class="arabic">فراولة</span></td>
          <td>Whole, halves, slices, diced</td>
          <td>Customer specifications / مواصفات حسب العميل</td>
        </tr>
        <tr>
          <td><strong>Green peas</strong> | <span class="arabic">بسلة خضراء</span></td>
          <td>Whole kernels; screened calibers</td>
          <td>Customer specifications / مواصفات حسب العميل</td>
        </tr>
        <tr>
          <td><strong>Green beans</strong> | <span class="arabic">فاصوليا خضراء</span></td>
          <td>Whole, cut</td>
          <td>Customer specifications / مواصفات حسب العميل</td>
        </tr>
        <tr>
          <td><strong>Okra</strong> | <span class="arabic">بامية</span></td>
          <td><strong>Extra , zero , one , two</strong></td>
          <td>Common lengths 2–5 cm; grade by agreement</td>
        </tr>
        <tr>
          <td><strong>Broccoli</strong> | <span class="arabic">بروكلي</span></td>
          <td>Florets, stem cuts</td>
          <td>Common floret grades 20–60 mm</td>
        </tr>
        <tr>
          <td><strong>Cauliflower</strong> | <span class="arabic">قرنبيط</span></td>
          <td>Florets</td>
          <td>Common floret grades 20–60 mm</td>
        </tr>
        <tr>
          <td><strong>Artichoke</strong> | <span class="arabic">خرشوف</span></td>
          <td><strong>Hearts, bottoms, quarters</strong></td>
          <td>Size / count per customer specification</td>
        </tr>
        <tr>
          <td><strong>Broad beans</strong> | <span class="arabic">فول أخضر</span></td>
          <td><strong>Peeled, unpeeled</strong></td>
          <td>Small / medium / large grades</td>
        </tr>
      </tbody>
    </table>

    <div class="callout emerald" style="margin-top: 5px;">
      <strong>Product Photography Gallery Note:</strong> In accordance with client instructions, each product card on the website incorporates interactive multi-photo gallery support (2 dedicated real photos per product) with modal zoom and lightbox inspection.
    </div>
  </div>

  <!-- ================= PAGE 5: PAGE 03 (OUR PRODUCTS) — PART 2 ================= -->
  <div class="doc-page">
    <div class="doc-header">
      <div class="brand">GREEN ALEX | IQF PRODUCTS PORTFOLIO</div>
      <div class="doc-type">Page 03 Product Catalogue (Part 2: Vegetables Continued & Processed)</div>
    </div>

    <div class="page-spec-header">
      <div class="page-title">PAGE 03 — OUR PRODUCTS (منتجاتنا) — PART 2</div>
      <div class="page-id">26-Product Portfolio Spec</div>
    </div>

    <h3 style="color: var(--navy-primary); border-bottom: 1.5px solid #0f766e; padding-bottom: 2px; margin-top: 2px;">B. IQF VEGETABLES (الخضروات المجمدة) — Continued (Items 9 to 16)</h3>
    <table>
      <thead>
        <tr>
          <th style="width: 25%;">Product (EN / AR)</th>
          <th style="width: 35%;">Available Styles / أشكال التصنيع</th>
          <th style="width: 40%;">Typical Commercial Sizes / مقاسات التقطيع والفرز</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Spinach</strong> | <span class="arabic">سبانخ</span></td>
          <td>Whole leaf, cut leaf, chopped</td>
          <td>Cutting style / particle size by agreement</td>
        </tr>
        <tr>
          <td><strong>Molokhia</strong> | <span class="arabic">ملوخية</span></td>
          <td>Minced, chopped, leaf</td>
          <td>Fine / coarse; customer specification</td>
        </tr>
        <tr>
          <td><strong>Sweet corn</strong> | <span class="arabic">ذرة حلوة</span></td>
          <td>Whole kernels</td>
          <td>Kernel grade / sweetness per specification</td>
        </tr>
        <tr>
          <td><strong>Sweet peppers</strong> | <span class="arabic">فلفل ألوان</span></td>
          <td>Strips, diced</td>
          <td>Customer specifications / مواصفات حسب العميل</td>
        </tr>
        <tr>
          <td><strong>Green onions (Spring onions)</strong> | <span class="arabic">بصل أخضر</span> <span class="badge badge-new">New</span></td>
          <td>Whole, chopped, sliced</td>
          <td>Customer specifications</td>
        </tr>
        <tr>
          <td><strong>Taro</strong> | <span class="arabic">قلقاس</span> <span class="badge badge-new">New</span></td>
          <td>Peeled, whole, diced, sliced</td>
          <td>Customer specifications</td>
        </tr>
        <tr>
          <td><strong>Pumpkin</strong> | <span class="arabic">قرع عسل</span> <span class="badge badge-new">New</span></td>
          <td>Peeled, diced, sliced</td>
          <td>Customer specifications</td>
        </tr>
        <tr>
          <td><strong>Sweet potatoes</strong> | <span class="arabic">بطاطا حلوة</span> <span class="badge badge-new">New</span></td>
          <td>Whole, diced, sliced, strips</td>
          <td>Customer specifications</td>
        </tr>
      </tbody>
    </table>

    <h3 style="color: var(--navy-primary); border-bottom: 1.5px solid #0f766e; padding-bottom: 2px; margin-top: 4px;">C. IQF MIXED VEGETABLES & PROCESSED (الخضروات المشكلة والمنتجات المصنعة) — 6 Products</h3>
    <table>
      <thead>
        <tr>
          <th style="width: 25%;">Product (EN / AR)</th>
          <th style="width: 35%;">Available Styles / أشكال التصنيع</th>
          <th style="width: 40%;">Typical Commercial Sizes / مقاسات التقطيع والفرز</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Mixed vegetables (Peas & Carrots)</strong> | <span class="arabic">خضروات مشكلة (بسلة وجزر)</span></td>
          <td>Whole peas and diced carrots</td>
          <td>Customer specifications / مواصفات حسب العميل</td>
        </tr>
        <tr>
          <td><strong>Mixed vegetables (Peas, Carrots & Green Beans)</strong> <span class="badge badge-new">New</span></td>
          <td>Whole peas, diced carrots and cut green beans</td>
          <td>Customer specifications</td>
        </tr>
        <tr>
          <td><strong>Mixed vegetables (Peas, Carrots, Green Beans & Sweet Corn)</strong> <span class="badge badge-new">New</span></td>
          <td>Whole peas, diced carrots, cut green beans and whole corn kernels</td>
          <td>Customer specifications</td>
        </tr>
        <tr>
          <td><strong>Mixed vegetables (Customized Blends)</strong> | <span class="arabic">خضروات مشكلة (خلطات مخصصة)</span></td>
          <td>Customized blends</td>
          <td>Ingredients and blend ratios by agreement</td>
        </tr>
        <tr>
          <td><strong>French fries</strong> | <span class="arabic">بطاطس نصف مقلية</span></td>
          <td>Straight cut</td>
          <td>Customer specifications / مواصفات حسب العميل</td>
        </tr>
        <tr>
          <td><strong>Falafel</strong> | <span class="arabic">فلافل / طعمية</span></td>
          <td>Balls and patties</td>
          <td>Weight and diameter by agreement</td>
        </tr>
      </tbody>
    </table>

    <div class="callout gold" style="margin-top: 4px; padding: 4px 8px; font-size: 7.2pt;">
      <strong>Approved Retail Packaging Brand: Virdi Va™ (العلامة التجارية المعتمدة للأكياس)</strong><br>
      Licensed retail brand for 400g consumer pillow packs (Green Beans, Green Peas, Diced Carrots, Frozen Strawberries, Molokhia, Okra). 100% natural, quick-frozen (-18°C), zero additives. Dual export capability: proprietary "Virdi Va™" brand or Buyer's Private Label.
    </div>

    <div class="disclaimer-box" style="margin-top: 4px; padding: 4px 8px;">
      <div class="disclaimer-title">IMPORTANT PRODUCT NOTE (OFFICIAL VERBATIM)</div>
      "Product forms and cutting sizes are common commercial options. Final specifications, grading, blend ratios and packaging requirements are agreed with each customer and confirmed through approved product specification sheets and samples."<br>
      <span class="arabic" style="display:block; margin-top: 1px; font-weight: 600;">
        "تنبيه هام: أشكال التصنيع ومقاسات التقطيع المذكورة أعلاه هي خيارات تجارية شائعة. يتم الاتفاق على المواصفات النهائية ودرجات الفرز ونسب الخلط واشتراطات التعبئة والتغليف مع كل عميل وتأكيدها عبر بطاقات مواصفات المنتج والعينات المعتمدة."
      </span>
    </div>
  </div>

  <!-- ================= DEDICATED PAGE: PACKAGING OPTIONS (أوزان وطرق التعبئة) ================= -->
  <div class="doc-page">
    <div class="doc-header">
      <div class="brand">GREEN ALEX | IQF PRODUCTS PORTFOLIO</div>
      <div class="doc-type">Packaging Options & Weights</div>
    </div>

    <div class="page-spec-header">
      <div class="page-title">PACKAGING OPTIONS | أوزان وطرق التعبئة</div>
      <div class="page-id">Export Formats</div>
    </div>

    <p style="font-size: 8.5pt; color: #475569; margin-bottom: 12px;">
      <strong>Available packaging formats and weights | أوزان وأشكال التعبئة المتاحة</strong>
    </p>

    <!-- Official Matrix Table -->
    <table style="margin-top: 10px; margin-bottom: 16px;">
      <thead>
        <tr style="background: #0f4c3a; color: #ffffff;">
          <th style="width: 25%; color: #ffffff;">Packaging Type</th>
          <th style="width: 25%; color: #ffffff; font-family: 'Cairo', sans-serif;">نوع التعبئة</th>
          <th style="width: 25%; color: #ffffff;">Weight</th>
          <th style="width: 25%; color: #ffffff; font-family: 'Cairo', sans-serif;">الوزن</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Plastic Bags</strong></td>
          <td class="arabic" style="font-weight: 700;">أكياس</td>
          <td><span style="display:inline-block; padding: 2px 8px; background: #e0f2fe; color: #0369a1; border-radius: 4px; font-weight: 700;">2,400 g</span></td>
          <td class="arabic"><span style="display:inline-block; padding: 2px 8px; background: #e0f2fe; color: #0369a1; border-radius: 4px; font-weight: 700;">٢,٤٠٠ جم</span></td>
        </tr>
        <tr>
          <td><strong>Plastic Bags</strong></td>
          <td class="arabic" style="font-weight: 700;">أكياس</td>
          <td><span style="display:inline-block; padding: 2px 8px; background: #e0f2fe; color: #0369a1; border-radius: 4px; font-weight: 700;">400 g</span></td>
          <td class="arabic"><span style="display:inline-block; padding: 2px 8px; background: #e0f2fe; color: #0369a1; border-radius: 4px; font-weight: 700;">٤٠٠ جم</span></td>
        </tr>
        <tr>
          <td><strong>Cartons</strong></td>
          <td class="arabic" style="font-weight: 700;">كراتين</td>
          <td><span style="display:inline-block; padding: 2px 8px; background: #fef3c7; color: #b45309; border-radius: 4px; font-weight: 700;">10 kg</span></td>
          <td class="arabic"><span style="display:inline-block; padding: 2px 8px; background: #fef3c7; color: #b45309; border-radius: 4px; font-weight: 700;">١٠ كجم</span></td>
        </tr>
        <tr>
          <td><strong>Woven Sacks</strong></td>
          <td class="arabic" style="font-weight: 700;">أجولة</td>
          <td><span style="display:inline-block; padding: 2px 8px; background: #e0f2fe; color: #0369a1; border-radius: 4px; font-weight: 700;">25 kg</span></td>
          <td class="arabic"><span style="display:inline-block; padding: 2px 8px; background: #e0f2fe; color: #0369a1; border-radius: 4px; font-weight: 700;">٢٥ كجم</span></td>
        </tr>
      </tbody>
    </table>

    <!-- 4 Sector Descriptions -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 16px;">
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 10px 12px;">
        <div style="font-size: 7.5pt; font-weight: 700; color: #059669; text-transform: uppercase;">Retail Shelves • عبوة تجزئة</div>
        <div style="font-size: 9.5pt; font-weight: 800; color: #0f172a; margin: 2px 0 4px;">400 g Plastic Pillow Pouches (أكياس)</div>
        <div style="font-size: 7.6pt; color: #475569; line-height: 1.45;">
          Consumer pillow pouches for supermarket display freezers. Supplied under the approved <strong>Virdi Va™</strong> brand or Buyer's Private Label.
        </div>
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 10px 12px;">
        <div style="font-size: 7.5pt; font-weight: 700; color: #059669; text-transform: uppercase;">Food Service • توريد فندقي</div>
        <div style="font-size: 9.5pt; font-weight: 800; color: #0f172a; margin: 2px 0 4px;">2,400 g Plastic Bags (أكياس)</div>
        <div style="font-size: 7.6pt; color: #475569; line-height: 1.45;">
          High-yield institutional pouches for hotels, restaurants, industrial kitchens, and catering contractors.
        </div>
      </div>
      <div style="background: #fefce8; border: 1px solid #fde047; border-radius: 6px; padding: 10px 12px;">
        <div style="font-size: 7.5pt; font-weight: 700; color: #b45309; text-transform: uppercase;">Export Standard • كرتون تصدير</div>
        <div style="font-size: 9.5pt; font-weight: 800; color: #0f172a; margin: 2px 0 4px;">10 kg Corrugated Master Cartons (كراتين)</div>
        <div style="font-size: 7.6pt; color: #475569; line-height: 1.45;">
          5-ply heavy-duty cartons with blue food-grade polyethylene inner liners, optimized for container seafreight palletization.
        </div>
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 10px 12px;">
        <div style="font-size: 7.5pt; font-weight: 700; color: #059669; text-transform: uppercase;">Industrial Bulk • توريد تصنيعي</div>
        <div style="font-size: 9.5pt; font-weight: 800; color: #0f172a; margin: 2px 0 4px;">25 kg Woven Polypropylene Sacks (أجولة)</div>
        <div style="font-size: 7.6pt; color: #475569; line-height: 1.45;">
          Heavy-duty sacks for large-scale food processors, jam/puree manufacturers, and industrial repackers.
        </div>
      </div>
    </div>

    <!-- Official Packaging Flexibility Callout -->
    <div class="callout emerald" style="padding: 12px 16px; margin-top: 10px; border-left: 4px solid #059669;">
      <div style="font-size: 9pt; font-weight: 800; color: #064e3b; margin-bottom: 4px;">
        Packaging Flexibility | مرونة التعبئة
      </div>
      <div style="font-size: 8.2pt; color: #0f172a; margin-bottom: 4px;">
        "Available in different packaging options according to customer requirements and product specifications."
      </div>
      <div class="arabic" style="font-size: 9pt; font-weight: 700; color: #064e3b;">
        "متاحة بأكثر من نظام تعبئة وفقاً لمتطلبات العملاء وطبيعة ومواصفات كل منتج."
      </div>
    </div>
  </div>

  <!-- ================= PAGE 7: PAGE 04 (SEASONAL HARVEST CALENDAR) ================= -->
  <div class="doc-page">
    <div class="doc-header">
      <div class="brand">GREEN ALEX | IQF PRODUCTS PORTFOLIO</div>
      <div class="doc-type">Page 04 Seasonal Harvest Calendar</div>
    </div>

    <div class="page-spec-header">
      <div class="page-title">PAGE 04 — SEASONAL HARVEST CALENDAR (التقويم الموسمي للحصاد)</div>
      <div class="page-id">Agricultural Schedule</div>
    </div>

    <p><strong>Primary Purpose:</strong> Present indicative Egyptian crop windows to enable foreign buyers to synchronize seasonal contracts with peak agricultural availability.</p>

    <div class="disclaimer-box">
      <div class="disclaimer-title">Official Agricultural Crop Window Disclaimer</div>
      "These are indicative Egyptian crop windows. Actual availability may vary by governorate, variety, weather conditions and farming schedule."<br>
      <span class="arabic" style="display:block; margin-top: 2px;">"الفترات التالية استرشادية للمحاصيل المصرية، وقد تختلف مواعيد التوافر الفعلية وفقاً للمحافظة والصنف والظروف الجوية والبرنامج الزراعي."</span>
    </div>

    <h3>1. Winter Crops (المحاصيل الشتوية)</h3>
    <table>
      <thead>
        <tr>
          <th style="width: 32%;">Crop Name (EN / AR)</th>
          <th style="width: 28%;">Indicative Peak Season</th>
          <th style="width: 40%;">Product Forms / أشكال التصنيع</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Strawberries</strong> | <span class="arabic">الفراولة</span></td>
          <td>December – April</td>
          <td>Whole, halves, slices, diced</td>
        </tr>
        <tr>
          <td><strong>Green peas / peas & carrots</strong> | <span class="arabic">البسلة والبسلة بالجزر</span></td>
          <td>November – March</td>
          <td>Whole peas; diced carrots; mixed blends</td>
        </tr>
        <tr>
          <td><strong>Broccoli & cauliflower</strong> | <span class="arabic">البروكلي والقرنبيط</span></td>
          <td>October – March</td>
          <td>IQF florets</td>
        </tr>
        <tr>
          <td><strong>Artichokes</strong> | <span class="arabic">الخرشوف</span></td>
          <td>Winter – early spring</td>
          <td>Hearts, bottoms, halves, quarters</td>
        </tr>
        <tr>
          <td><strong>Broad beans (Foul)</strong> | <span class="arabic">الفول الأخضر</span></td>
          <td>Winter</td>
          <td>Peeled / unpeeled / halves</td>
        </tr>
        <tr>
          <td><strong>Spinach & Molokhia</strong> | <span class="arabic">السبانخ والملوخية</span></td>
          <td>Winter – spring</td>
          <td>Whole leaf / chopped / minced</td>
        </tr>
      </tbody>
    </table>

    <h3>2. Summer Crops (المحاصيل الصيفية)</h3>
    <table>
      <thead>
        <tr>
          <th style="width: 32%;">Crop Name (EN / AR)</th>
          <th style="width: 28%;">Indicative Peak Season</th>
          <th style="width: 40%;">Product Forms / أشكال التصنيع</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Mango (Keitt, Kent, Yasmina)</strong> | <span class="arabic">المانجو</span></td>
          <td>July – October (Peak: Aug–Sep)</td>
          <td>Diced / chunks / slices</td>
        </tr>
        <tr>
          <td><strong>Okra (Bamia)</strong> | <span class="arabic">البامية</span></td>
          <td>April – September / October</td>
          <td>Baby whole (zero) / whole / cut</td>
        </tr>
        <tr>
          <td><strong>Green beans</strong> | <span class="arabic">الفاصوليا الخضراء</span></td>
          <td>April – July (Secondary: Oct–Jan)</td>
          <td>Whole / cut / French cut</td>
        </tr>
        <tr>
          <td><strong>Pomegranate arils</strong> | <span class="arabic">حبوب الرمان</span></td>
          <td>September – December</td>
          <td>Cleaned whole arils</td>
        </tr>
        <tr>
          <td><strong>Sweet corn & peppers</strong> | <span class="arabic">الذرة الحلوة والفلفل</span></td>
          <td>Summer harvest window</td>
          <td>Kernels / strips / diced</td>
        </tr>
      </tbody>
    </table>

    <h3>3. Year-Round / Processed Items (منتجات متاحة على مدار العام)</h3>
    <div class="callout emerald" style="margin-top: 4px;">
      <strong>French fries, mixed vegetables, and falafel:</strong> May be produced or supplied throughout the year, subject to raw-material sourcing, production planning, and customer demand.<br>
      <span class="arabic" style="display:block; margin-top:2px;">البطاطس نصف المقلية، الخضروات المشكلة، والفلافل: متاحة على مدار العام وفقاً لتوافر الخامات وخطة الإنتاج واحتياجات العملاء.</span>
    </div>
  </div>

  <!-- ================= PAGE 7: PAGE 05 (QUALITY & FOOD SAFETY) ================= -->
  <div class="doc-page">
    <div class="doc-header">
      <div class="brand">GREEN ALEX | IQF PRODUCTS PORTFOLIO</div>
      <div class="doc-type">Page 05 Quality & Food Safety Architecture</div>
    </div>

    <div class="page-spec-header">
      <div class="page-title">PAGE 05 — QUALITY & FOOD SAFETY (الجودة وسلامة الغذاء)</div>
      <div class="page-id">Standards & Compliance Spec</div>
    </div>

    <p style="margin-bottom: 4px;"><strong>Primary Purpose:</strong> Present applicable Egyptian and international standards, core quality control points, and explicit compliance parameters.</p>

    <h3 style="margin-top: 3px;">A. Egyptian EOS Standards (المواصفات القياسية المصرية)</h3>
    <table>
      <thead>
        <tr>
          <th style="width: 22%;">Standard No.</th>
          <th style="width: 40%;">Subject / عنوان المواصفة</th>
          <th style="width: 38%;">Portfolio Note & Regulatory Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>ES 2368 / 2021</strong></td>
          <td>Quick Frozen Strawberries | <span class="arabic">الفراولة سريعة التجميد</span></td>
          <td><span class="badge badge-obligatory">Obligatory</span> EOS catalogue lists as obligatory.</td>
        </tr>
        <tr>
          <td><strong>ES 1676 / 2005</strong></td>
          <td>Frozen Mixed Vegetables | <span class="arabic">الخضروات المشكلة المجمدة</span></td>
          <td><span class="badge badge-obligatory">Obligatory</span> Status shown as total modification.</td>
        </tr>
        <tr>
          <td><strong>ES 1681 / 2005</strong></td>
          <td>Frozen Jew's Mallow (Molokhia) | <span class="arabic">الملوخية المجمدة</span></td>
          <td><span class="badge badge-verify">Verify</span> Listed in EOS catalogue; verify current text.</td>
        </tr>
        <tr>
          <td><strong>ES 1702 / 2005</strong></td>
          <td>Frozen Okra | <span class="arabic">البامية المجمدة</span></td>
          <td><span class="badge badge-obligatory">Obligatory</span> Status shown as total modification.</td>
        </tr>
        <tr>
          <td><strong>ES 1743 / 2014</strong></td>
          <td>Frozen Green Beans | <span class="arabic">الفاصوليا الخضراء المجمدة</span></td>
          <td><span class="badge badge-updated">Updated</span> Obligatory; status updated.</td>
        </tr>
        <tr>
          <td><strong>ES 1746 / 2005</strong></td>
          <td>Frozen Artichoke | <span class="arabic">الخرشوف المجمد</span></td>
          <td><span class="badge badge-verify">Verify</span> Listed in EOS catalogue; verify text.</td>
        </tr>
        <tr>
          <td><strong>ES 1748 / 2014</strong></td>
          <td>Quick Frozen Peas | <span class="arabic">البسلة سريعة التجميد</span></td>
          <td><span class="badge badge-obligatory">Obligatory</span> Verify current edition and status.</td>
        </tr>
        <tr>
          <td><strong>ES 1749 / 2014</strong></td>
          <td>Frozen Green Spinach | <span class="arabic">السبانخ الخضراء المجمدة</span></td>
          <td><span class="badge badge-obligatory">Obligatory</span> Verify current edition and status.</td>
        </tr>
        <tr>
          <td><strong>ES 991 / 2008</strong></td>
          <td>Methods of Analysis & Testing of Frozen Veg.</td>
          <td><span class="badge badge-standard">Testing Method</span> Non-obligatory test method standard.</td>
        </tr>
      </tbody>
    </table>
    <div style="font-size: 7pt; color: #64748b; margin-top: -4px; margin-bottom: 5px;">
      Official Source: EOS online standards catalogue: <a href="https://www.eos.org.eg/en/standards" style="color: #0f766e;">https://www.eos.org.eg/en/standards</a>
    </div>

    <h3 style="margin-top: 3px;">B. International References (المراجع والمواصفات الدولية)</h3>
    <table>
      <thead>
        <tr>
          <th style="width: 25%;">Reference Code</th>
          <th style="width: 35%;">Title</th>
          <th style="width: 40%;">Scope & Technical Relevance</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Codex CXS 320-2015</strong></td>
          <td>Standard for Quick-Frozen Vegetables</td>
          <td>Product definition, quality factors, defects, contaminants, labelling.</td>
        </tr>
        <tr>
          <td><strong>Codex CXC 8-1976</strong></td>
          <td>Code of Practice for Quick-Frozen Foods</td>
          <td>Good handling practices, freezing, storage, and distribution.</td>
        </tr>
        <tr>
          <td><strong>Codex CXS 1-1985</strong></td>
          <td>General Standard for Labelling Prepackaged Foods</td>
          <td>Food-label information and mandatory declarations.</td>
        </tr>
        <tr>
          <td><strong>Codex CXS 193-1995</strong></td>
          <td>General Standard for Contaminants in Food</td>
          <td>Permitted contaminant threshold limits.</td>
        </tr>
        <tr>
          <td><strong>Codex Pesticide MRLs</strong></td>
          <td>Maximum Residue Limits for Pesticides</td>
          <td>Check commodity/pesticide combinations and market limits.</td>
        </tr>
        <tr>
          <td><strong>ISO 22000:2018</strong></td>
          <td>Food Safety Management Systems</td>
          <td>FSMS framework; certification by accredited body.</td>
        </tr>
        <tr>
          <td><strong>HACCP / CXC 1-1969</strong></td>
          <td>General Principles of Food Hygiene</td>
          <td>HACCP hazard analysis and critical preventive controls.</td>
        </tr>
        <tr>
          <td><strong>BRCGS / IFS Food</strong></td>
          <td>GFSI-Recognized Schemes</td>
          <td>Customer / retailer-driven certification schemes where required.</td>
        </tr>
      </tbody>
    </table>

    <h3 style="margin-top: 3px;">C. Core IQF Quality Control Points (نقاط الفحص الأساسية)</h3>
    <div class="grid-2">
      <div class="info-card" style="padding: 4px 7px;">
        <p style="font-size: 7.3pt; margin: 0;">
          <strong>1. Raw Material:</strong> Approved source, maturity, freshness, incoming inspection.<br>
          <strong>2. Preparation:</strong> Washing, sorting, trimming, peeling, cutting to spec.<br>
          <strong>3. Blanching:</strong> Enzyme inactivation applied where validated.<br>
          <strong>4. Freezing:</strong> Target -18°C or colder at thermal center.
        </p>
      </div>
      <div class="info-card" style="padding: 4px 7px;">
        <p style="font-size: 7.3pt; margin: 0;">
          <strong>5. Finished Product:</strong> Colour, flavour, texture, defects, pack integrity.<br>
          <strong>6. Food Safety:</strong> Micro/chemical/physical hazard controls; MRL testing.<br>
          <strong>7. Cold Chain:</strong> Continuous -18°C through storage and export distribution.<br>
          <strong>8. Traceability:</strong> Batch coding, production records, temperature logging.
        </p>
      </div>
    </div>

    <div class="disclaimer-box" style="margin-top: 4px;">
      <div class="disclaimer-title">Mandatory Legal Compliance Disclaimer (Preserved Exactly)</div>
      "Listing a standard on this website does not mean that GREEN ALEX is certified to that standard, nor does it mean that every listed standard applies to every product. The current official text, status and scope must be verified with EOS and the competent authority. Destination markets and individual customers may impose additional requirements."
    </div>
  </div>

  <!-- ================= PAGE 8: PAGE 06 (CONTACT US) & CLIENT APPROVAL ================= -->
  <div class="doc-page">
    <div class="doc-header">
      <div class="brand">GREEN ALEX | IQF PRODUCTS PORTFOLIO</div>
      <div class="doc-type">Page 06 Contact & Client Approval Checklist</div>
    </div>

    <div class="page-spec-header">
      <div class="page-title">PAGE 06 — CONTACT US (اتصل بنا)</div>
      <div class="page-id">B2B Channel Spec</div>
    </div>

    <p><strong>Primary Purpose:</strong> Present verified physical headquarters, commercial registration, and direct communication channels for overseas B2B trade partners.</p>

    <div class="grid-2">
      <div class="info-card">
        <h4>Confirmed Corporate Contact Credentials</h4>
        <p style="font-size: 7.7pt; margin: 0;">
          <strong>Company Name:</strong> GREEN ALEX<br>
          <strong>Administration Office:</strong> 10 Ibn Shogaa Street, Al-Azareeta, Alexandria, Egypt.<br>
          <strong>Commercial Registration:</strong> Rashid, Beheira Governorate, Egypt.<br>
          <strong>Established:</strong> 1999.<br>
          <strong>Founder / Owner:</strong> <strong>Dr. Mohamed Gabr</strong>.<br>
          <strong>Direct WhatsApp / Mobile:</strong> <strong>+20 109 300 3736</strong> (01093003736).
        </p>
      </div>

      <div class="info-card" style="border-left: 3.5px solid var(--gold-accent);">
        <h4>Missing Info Checklist for Client Confirmation:</h4>
        <div class="checklist-item"><div class="checkbox"></div> <span><strong>Corporate Export Email:</strong> (e.g., export@greenalex.com)</span></div>
        <div class="checklist-item"><div class="checkbox"></div> <span><strong>Official Domain:</strong> (e.g., www.greenalex.com)</span></div>
        <div class="checklist-item"><div class="checkbox"></div> <span><strong>Social Media:</strong> (LinkedIn Company Page)</span></div>
        <div class="checklist-item"><div class="checkbox"></div> <span><strong>Fixed Landline Office Number:</strong> (Alexandria Office)</span></div>
      </div>
    </div>

    <h2 style="margin-top: 8px; border-bottom: 2px solid var(--gold-accent);">CLIENT REVIEW & APPROVAL CHECKLIST</h2>
    <p style="font-size: 7.8pt; margin-bottom: 5px;">
      "Please review the proposed website structure and content allocation. You may approve the structure as presented or provide comments and corrections for any page or section. Once the content structure is approved, we can proceed to the visual design stage."
    </p>

    <table>
      <thead>
        <tr>
          <th style="width: 7%;">Check</th>
          <th style="width: 33%;">Review Item</th>
          <th style="width: 45%;">Scope Verified</th>
          <th style="width: 15%;">Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="text-align: center;"><div class="checkbox" style="margin: 0 auto;"></div></td>
          <td><strong>1. Six Proposed Website Pages</strong></td>
          <td>Home, About Us, Products, Harvest Calendar, Quality & Safety, Contact Us.</td>
          <td>Pending Client</td>
        </tr>
        <tr>
          <td style="text-align: center;"><div class="checkbox" style="margin: 0 auto;"></div></td>
          <td><strong>2. Home Page Content</strong></td>
          <td>Tagline, 1999 heritage, Dr. Mohamed Gabr, category previews.</td>
          <td>Pending Client</td>
        </tr>
        <tr>
          <td style="text-align: center;"><div class="checkbox" style="margin: 0 auto;"></div></td>
          <td><strong>3. About Us Profile</strong></td>
          <td>Heritage text, bilingual parity, customization parameters.</td>
          <td>Pending Client</td>
        </tr>
        <tr>
          <td style="text-align: center;"><div class="checkbox" style="margin: 0 auto;"></div></td>
          <td><strong>4. 26 Products & Commercial Sizes</strong></td>
          <td>5 Fruits, 15 Vegetables, 6 Mixed & Processed, all styles & sizes.</td>
          <td>Pending Client</td>
        </tr>
        <tr>
          <td style="text-align: center;"><div class="checkbox" style="margin: 0 auto;"></div></td>
          <td><strong>5. Product Photography</strong></td>
          <td>Multi-photo gallery support (2 dedicated real photos per product).</td>
          <td>Pending Client</td>
        </tr>
        <tr>
          <td style="text-align: center;"><div class="checkbox" style="margin: 0 auto;"></div></td>
          <td><strong>6. Seasonal Harvest Calendar</strong></td>
          <td>Winter, Summer, and Year-Round windows and crop disclaimer.</td>
          <td>Pending Client</td>
        </tr>
        <tr>
          <td style="text-align: center;"><div class="checkbox" style="margin: 0 auto;"></div></td>
          <td><strong>7. Standards & Quality References</strong></td>
          <td>9 EOS standards, 8 international references, QC pipeline.</td>
          <td>Pending Client</td>
        </tr>
        <tr>
          <td style="text-align: center;"><div class="checkbox" style="margin: 0 auto;"></div></td>
          <td><strong>8. Contact & WhatsApp Routing</strong></td>
          <td>Alexandria / Rashid offices and WhatsApp (+201093003736).</td>
          <td>Pending Client</td>
        </tr>
        <tr>
          <td style="text-align: center;"><div class="checkbox" style="margin: 0 auto;"></div></td>
          <td><strong>9. Arabic & English Bilingual Content</strong></td>
          <td>Full bilingual text and correct Arabic rendering throughout.</td>
          <td>Pending Client</td>
        </tr>
      </tbody>
    </table>

    <div class="info-card" style="margin-top: 6px; background: #fafafa;">
      <h4 style="color: var(--navy-primary); margin-bottom: 4px;">Client Approval & Sign-Off Authorization</h4>
      <div class="grid-2">
        <div>
          <p style="font-size: 7.6pt; margin: 0;">
            <strong>Reviewed By:</strong> ___________________________________<br><br>
            <strong>Title / Position:</strong> ___________________________________<br><br>
            <strong>Signature:</strong> ___________________________________
          </p>
        </div>
        <div>
          <p style="font-size: 7.6pt; margin: 0;">
            <strong>Approval Date:</strong> ____ / ____ / 2026<br><br>
            <strong>Status:</strong> [ &nbsp; ] Approved As Is &nbsp;&nbsp;&nbsp; [ &nbsp; ] Approved with Amendments<br><br>
            <strong>Comments:</strong> ___________________________________
          </p>
        </div>
      </div>
    </div>
  </div>

</body>
</html>
"""

    with open('proposal.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("proposal.html written successfully.")

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    output_pdf = os.path.abspath("GREEN_ALEX_Website_Portfolio_Structure_Review_Updated.pdf")
    input_html = os.path.abspath("proposal.html")

    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf}",
        input_html
    ]

    print("Running Chrome print-to-pdf...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Return code:", res.returncode)
    print("Stderr:", res.stderr)
    
    if os.path.exists(output_pdf):
        size = os.path.getsize(output_pdf)
        print(f"PDF successfully created: {output_pdf} (Size: {size} bytes)")
        reader = PdfReader(output_pdf)
        print(f"Total pages rendered in PDF: {len(reader.pages)}")
        
        # Also attempt to copy to GREEN_ALEX_Website_Portfolio_Structure_Review.pdf if not locked
        import shutil
        target_orig = os.path.abspath("GREEN_ALEX_Website_Portfolio_Structure_Review.pdf")
        try:
            shutil.copyfile(output_pdf, target_orig)
            print("Also updated GREEN_ALEX_Website_Portfolio_Structure_Review.pdf successfully.")
        except Exception as e:
            print("Notice: Original PDF name is currently locked in an external viewer. Updated PDF saved as GREEN_ALEX_Website_Portfolio_Structure_Review_Updated.pdf.")

if __name__ == '__main__':
    generate_pdf()
