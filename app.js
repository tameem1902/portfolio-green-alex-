/* ==========================================================================
   GREEN ALEX — Frontend Application Logic & Data Controller
   Updated with ALL Additional Products & Latest Commercial Modifications
   ========================================================================== */

// 1. Complete Product Data Structure (26 Export Products)
const PRODUCTS = [
  // ==========================================
  // Category A: IQF Fruits (4 Products)
  // ==========================================
  {
    id: 'mango',
    category: 'fruits',
    nameEn: 'Mango',
    nameAr: 'مانجو',
    image: 'assets/images/prod_mango.jpg?v=20261103_v8',
    gallery: ['assets/images/prod_mango.jpg?v=20261103_v8'],
    stylesEn: 'Diced, chunks, slices (Keitt, Kent, Yasmina)',
    stylesAr: 'مكعبات، قطع، شرائح (كيت، كينت، ياسمينا)',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'July – October (Peak: Aug–Sep)',
    harvestAr: 'يوليو – أكتوبر (الذروة: أغسطس وسبتمبر)',
    packaging: '10 kg bulk export carton / 1 kg food service packs',
    temp: '-18°C or colder'
  },
  {
    id: 'pomegranate',
    category: 'fruits',
    nameEn: 'Pomegranate arils',
    nameAr: 'حبوب رمان',
    image: 'assets/images/prod_pomegranate.jpg?v=20261103_v8',
    gallery: ['assets/images/prod_pomegranate.jpg?v=20261103_v8'],
    stylesEn: 'Cleaned whole arils (Ruby red)',
    stylesAr: 'حبوب كاملة منقاة ومفروزة',
    sizesEn: 'Customer specification / حسب مواصفة العميل',
    sizesAr: 'حسب مواصفة العميل / Customer specification',
    harvestEn: 'September – December',
    harvestAr: 'سبتمبر – ديسمبر',
    packaging: '10 kg bulk cartons / Octabin / 500g pouches',
    temp: '-18°C or colder'
  },
  {
    id: 'figs',
    category: 'fruits',
    nameEn: 'Figs',
    nameAr: 'تين',
    image: 'assets/images/prod_figs.jpg?v=20261104_v6',
    gallery: [
      'assets/images/prod_figs.jpg?v=20261104_v6'
    ],
    stylesEn: 'Whole, halves, quarters, diced',
    stylesAr: 'كامل، أنصاف، أرباع، مكعبات',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'Summer – early autumn',
    harvestAr: 'الصيف وبداية الخريف',
    packaging: '10 kg bulk export cartons / retail pouches',
    temp: '-18°C or colder'
  },
  {
    id: 'apricot',
    category: 'fruits',
    nameEn: 'Apricot',
    nameAr: 'مشمش',
    image: 'assets/images/prod_apricot.jpg?v=20261104_v5',
    gallery: [
      'assets/images/prod_apricot_halves.jpg?v=20261104_v5'
    ],
    stylesEn: 'Halves, quarters, diced',
    stylesAr: 'أنصاف، أرباع، مكعبات',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'Late spring – early summer',
    harvestAr: 'أواخر الربيع وبداية الصيف',
    packaging: '10 kg bulk export cartons / 1 kg packs',
    temp: '-18°C or colder'
  },
{
    id: 'strawberry',
    category: 'fruits',
    nameEn: 'Strawberry',
    nameAr: 'فراولة',
    image: 'assets/images/prod_strawberry.jpg?v=20261104',
    gallery: [
      'assets/images/prod_strawberry_whole.jpg?v=20261104',
      'assets/images/prod_strawberry_diced.jpg?v=20261104'
    ],
    stylesEn: 'Whole, halves, slices, diced',
    stylesAr: 'كاملة، أنصاف، شرائح، مكعبات',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'December – April (Winter peak)',
    harvestAr: 'ديسمبر – أبريل (ذروة الشتاء)',
    packaging: '10 kg bulk poly-lined export carton / 400g & 1kg retail pillow packs',
    temp: '-18°C or colder'
  },

  // ==========================================
  // Category B: IQF Vegetables (15 Products)
  // ==========================================
  {
    id: 'green-peas',
    category: 'vegetables',
    nameEn: 'Green peas',
    nameAr: 'بسلة خضراء',
    image: 'assets/images/prod_green_peas.jpg?v=20261104_v8',
    gallery: [
      'assets/images/prod_green_peas.jpg?v=20261104_v8'
    ],
    stylesEn: 'Whole kernels',
    stylesAr: 'حبوب كاملة',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'November – March',
    harvestAr: 'نوفمبر – مارس',
    packaging: '10 kg bulk cartons / 400g retail pillow pouches',
    temp: '-18°C or colder'
  },
  {
    id: 'green-beans',
    category: 'vegetables',
    nameEn: 'Green beans',
    nameAr: 'فاصوليا خضراء',
    image: 'assets/images/prod_green_beans.jpg?v=20261103_v8',
    gallery: ['assets/images/prod_green_beans.jpg?v=20261103_v8'],
    stylesEn: 'Whole, cut',
    stylesAr: 'كاملة، مقطعة',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'April – July; secondary Oct–Jan',
    harvestAr: 'أبريل – يوليو؛ وموسم ثانٍ أكتوبر – يناير',
    packaging: '10 kg bulk cartons / 400g retail',
    temp: '-18°C or colder'
  },
  {
    id: 'okra',
    category: 'vegetables',
    nameEn: 'Okra (Bamia)',
    nameAr: 'بامية',
    image: 'assets/images/prod_okra.jpg?v=20261104_v2',
    gallery: [
      'assets/images/prod_okra_whole.jpg?v=20261104_v2',
      'assets/images/prod_okra_factory.jpg?v=20261104_v2'
    ],
    stylesEn: 'Extra , zero , one , two',
    stylesAr: 'إكسترا ، زيرو ، نمرة 1 ، نمرة 2',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'April – September / October',
    harvestAr: 'أبريل – سبتمبر / أكتوبر',
    packaging: '10 kg bulk cartons / 400g bags',
    temp: '-18°C or colder'
  },
  {
    id: 'broccoli',
    category: 'vegetables',
    nameEn: 'Broccoli',
    nameAr: 'بروكلي',
    image: 'assets/images/prod_broccoli.jpg?v=20261104_v3',
    gallery: [
      'assets/images/prod_broccoli_box.jpg?v=20261104_v3',
      'assets/images/prod_broccoli_conveyor.jpg?v=20261104_v3'
    ],
    stylesEn: 'Florets',
    stylesAr: 'زهرات IQF',
    sizesEn: 'Common floret grades 20–60 mm',
    sizesAr: 'أحجام الزهرات الشائعة: 20–60 مم',
    harvestEn: 'October – March',
    harvestAr: 'أكتوبر – مارس',
    packaging: '10 kg bulk cartons / 1kg food service',
    temp: '-18°C or colder'
  },
  {
    id: 'cauliflower',
    category: 'vegetables',
    nameEn: 'Cauliflower',
    nameAr: 'قرنبيط',
    image: 'assets/images/prod_cauliflower.jpg?v=20261104_v2',
    gallery: [
      'assets/images/prod_cauliflower_trays.jpg?v=20261104_v2',
      'assets/images/prod_cauliflower_sorting.jpg?v=20261104_v2'
    ],
    stylesEn: 'Florets',
    stylesAr: 'زهرات IQF مفروزة',
    sizesEn: 'Common floret grades 20–60 mm',
    sizesAr: 'أحجام الزهرات الشائعة: 20–60 مم',
    harvestEn: 'October – March',
    harvestAr: 'أكتوبر – مارس',
    packaging: '10 kg bulk cartons / 400g retail',
    temp: '-18°C or colder'
  },
  {
    id: 'artichoke',
    category: 'vegetables',
    nameEn: 'Artichoke',
    nameAr: 'خرشوف',
    image: 'assets/images/prod_artichoke.jpg?v=20261104_v4',
    gallery: [
      'assets/images/prod_artichoke_bottoms.jpg?v=20261104_v4',
      'assets/images/prod_artichoke_quarters.jpg?v=20261104_v4'
    ],
    stylesEn: 'Hearts, bottoms, quarters',
    stylesAr: 'قلوب، قواعد، أرباع',
    sizesEn: 'Size / count per customer specification',
    sizesAr: 'المقاس والعدد حسب مواصفة العميل',
    harvestEn: 'Winter – early spring',
    harvestAr: 'الشتاء وبداية الربيع',
    packaging: '10 kg bulk cartons / specialized catering packs',
    temp: '-18°C or colder'
  },
  {
    id: 'broad-beans',
    category: 'vegetables',
    nameEn: 'Broad beans (Foul)',
    nameAr: 'فول أخضر',
    image: 'assets/images/prod_broad_beans.jpg?v=20261104_v8',
    gallery: [
      'assets/images/prod_broad_beans.jpg?v=20261104_v8'
    ],
    stylesEn: 'Peeled, unpeeled',
    stylesAr: 'مقشر، بقشره',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'Winter season',
    harvestAr: 'موسم الشتاء',
    packaging: '10 kg bulk cartons / 400g bags',
    temp: '-18°C or colder'
  },
  {
    id: 'spinach',
    category: 'vegetables',
    nameEn: 'Spinach',
    nameAr: 'سبانخ',
    image: 'assets/images/prod_spinach.jpg?v=20261104',
    gallery: [
      'assets/images/prod_spinach_cubes.jpg?v=20261104',
      'assets/images/prod_spinach_pouches.jpg?v=20261104'
    ],
    stylesEn: 'Whole leaf, cut leaf, chopped',
    stylesAr: 'أوراق كاملة، مقطعة، مفرومة',
    sizesEn: 'Cutting style / particle size by agreement',
    sizesAr: 'نمط التقطيع وحجم الجزيئات بالاتفاق',
    harvestEn: 'Winter – spring',
    harvestAr: 'الشتاء والربيع',
    packaging: '10 kg bulk cartons / blocks / 400g bags',
    temp: '-18°C or colder'
  },
  {
    id: 'molokhia',
    category: 'vegetables',
    nameEn: 'Molokhia (Jew’s Mallow)',
    nameAr: 'ملوخية',
    image: 'assets/images/prod_molokhia.jpg?v=20261104_v7',
    gallery: [
      'assets/images/prod_molokhia.jpg?v=20261104_v7'
    ],
    stylesEn: 'Minced, chopped, leaf',
    stylesAr: 'مفرومة ناعم، مجروشة، أوراق',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'Winter – spring',
    harvestAr: 'الشتاء والربيع',
    packaging: '400g retail pouches (20 packs / carton)',
    temp: '-18°C or colder'
  },
  {
    id: 'sweet-corn',
    category: 'vegetables',
    nameEn: 'Sweet corn',
    nameAr: 'ذرة حلوة',
    image: 'assets/images/prod_sweet_corn.jpg?v=20261104_v6',
    gallery: [
      'assets/images/prod_corn_kernels.jpg?v=20261104_v6',
      'assets/images/prod_corn_cobs.jpg?v=20261104_v6'
    ],
    stylesEn: 'Whole kernels, cut cobs, sweet corn half cob and whole cob',
    stylesAr: 'حبوب كاملة مفرزة، قطع كيزان، أنصاف كيزان وكيزان كاملة',
    sizesEn: 'Kernel grade / sweetness per specification',
    sizesAr: 'درجة الحبوب ونسبة الحلاوة حسب المواصفة',
    harvestEn: 'Summer harvest window',
    harvestAr: 'فترة الحصاد الصيفية',
    packaging: '10 kg bulk cartons / 400g bags',
    temp: '-18°C or colder'
  },
  {
    id: 'sweet-peppers',
    category: 'vegetables',
    nameEn: 'Sweet peppers',
    nameAr: 'فلفل ألوان',
    image: 'assets/images/prod_sweet_peppers.jpg?v=20261104_v9',
    gallery: [
      'assets/images/prod_sweet_peppers.jpg?v=20261104_v9'
    ],
    stylesEn: 'Strips, diced',
    stylesAr: 'شرائح طولية، مكعبات',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'Summer harvest window',
    harvestAr: 'فترة الحصاد الصيفية',
    packaging: '10 kg bulk cartons / customized catering packs',
    temp: '-18°C or colder'
  },
  {
    id: 'green-onions',
    category: 'vegetables',
    nameEn: 'Green onion and onion',
    nameAr: 'بصل وبصل أخضر',
    image: 'assets/images/prod_green_onions.jpg?v=20261104_v5',
    gallery: [
      'assets/images/prod_green_onions_caliper.jpg?v=20261104_v5',
      'assets/images/prod_green_onions_batch.jpg?v=20261104_v5',
      'assets/images/prod_onion_box.jpg?v=20261104_v5',
      'assets/images/prod_onion_diced.jpg?v=20261104_v5'
    ],
    stylesEn: 'Chopped, sliced, diced, whole',
    stylesAr: 'مقطع حلقات، مفروم، مكعبات، كامل',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'Winter – spring',
    harvestAr: 'الشتاء والربيع',
    packaging: '10 kg bulk cartons / food service packs',
    temp: '-18°C or colder'
  },
  {
    id: 'taro',
    category: 'vegetables',
    nameEn: 'Taro',
    nameAr: 'قلقاس',
    image: 'assets/images/prod_taro.jpg?v=20261104_v6',
    gallery: [
      'assets/images/prod_taro.jpg?v=20261104_v6'
    ],
    stylesEn: 'Diced',
    stylesAr: 'مكعبات',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'Autumn – winter',
    harvestAr: 'الخريف والشتاء',
    packaging: '10 kg bulk cartons / 400g retail bags',
    temp: '-18°C or colder'
  },
  {
    id: 'pumpkin',
    category: 'vegetables',
    nameEn: 'Pumpkin',
    nameAr: 'قرع عسل',
    image: 'assets/images/prod_pumpkin.jpg?v=20261104_v7',
    gallery: [
      'assets/images/prod_pumpkin.jpg?v=20261104_v7'
    ],
    stylesEn: 'Diced',
    stylesAr: 'مكعبات',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'Autumn – early winter',
    harvestAr: 'الخريف وبداية الشتاء',
    packaging: '10 kg bulk cartons / industrial processing totes',
    temp: '-18°C or colder'
  },
  {
    id: 'sweet-potatoes',
    category: 'vegetables',
    nameEn: 'Sweet potatoes',
    nameAr: 'بطاطا حلوة',
    image: 'assets/images/prod_sweet_potatoes.jpg?v=20261104_v8',
    gallery: [
      'assets/images/prod_sweet_potatoes.jpg?v=20261104_v8'
    ],
    stylesEn: 'Diced, sliced, strips',
    stylesAr: 'مكعبات، شرائح، أصابع',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'August – February',
    harvestAr: 'أغسطس – فبراير',
    packaging: '10 kg bulk export cartons / retail polybags',
    temp: '-18°C or colder'
  },

  // ==========================================
  // Category C: IQF Mixed Vegetables & Processed (6 Products)
  // ==========================================
  {
    id: 'mixed-peas-carrots',
    category: 'processed',
    nameEn: 'Mixed vegetables (Peas & Carrots)',
    nameAr: 'خضروات مشكلة (بسلة وجزر)',
    image: 'assets/images/cat_processed.jpg?v=20261104_v7',
    stylesEn: 'Whole peas and diced carrots',
    stylesAr: 'حبوب بسلة وجزر مكعبات',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'Year-Round supply capability',
    harvestAr: 'متاحة للتوريد على مدار العام',
    packaging: '10 kg bulk cartons / 400g & 1kg retail pouches',
    temp: '-18°C or colder'
  },
  {
    id: 'mixed-3way',
    category: 'processed',
    nameEn: 'Mixed vegetables (Peas, Carrots & Green Beans)',
    nameAr: 'خضروات مشكلة (بسلة، جزر، فاصوليا خضراء)',
    image: 'assets/images/prod_mixed_3way.jpg?v=20261103_v8',
    gallery: ['assets/images/prod_mixed_3way.jpg?v=20261103_v8'],
    stylesEn: 'Whole peas, diced carrots and cut green beans',
    stylesAr: 'حبوب بسلة، جزر مكعبات، فاصوليا خضراء مقطعة',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'Year-Round supply capability',
    harvestAr: 'متاحة للتوريد على مدار العام',
    packaging: '10 kg bulk cartons / 400g & 1kg retail pouches',
    temp: '-18°C or colder'
  },
  {
    id: 'mixed-4way',
    category: 'processed',
    nameEn: 'Mixed vegetables (Peas, Carrots, Green Beans & Sweet Corn)',
    nameAr: 'خضروات مشكلة (بسلة، جزر، فاصوليا، ذرة حلوة)',
    image: 'assets/images/prod_mixed_4way.jpg?v=20261104_v7',
    gallery: [
      'assets/images/prod_mixed_4way.jpg?v=20261104_v7',
      'assets/images/cat_processed.jpg?v=20261104_v7'
    ],
    stylesEn: 'Whole peas, diced carrots, cut green beans and whole corn kernels',
    stylesAr: 'حبوب بسلة، جزر مكعبات، فاصوليا مقطعة، وحبوب ذرة كاملة',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'Year-Round supply capability',
    harvestAr: 'متاحة للتوريد على مدار العام',
    packaging: '10 kg bulk cartons / 400g & 1kg retail pouches',
    temp: '-18°C or colder'
  },
  {
    id: 'custom-blends',
    category: 'processed',
    nameEn: 'Mixed vegetables (Customized Blends)',
    nameAr: 'خضروات مشكلة (خلطات مخصصة)',
    image: 'assets/images/cat_processed.jpg?v=20261104_v7',
    stylesEn: 'Customized blends to buyer formula',
    stylesAr: 'خلطات مخصصة وفق تركيبة العميل',
    sizesEn: 'Ingredients and blend ratios by agreement',
    sizesAr: 'المكونات ونسب الخلط باتفاق العميل',
    harvestEn: 'Year-Round supply capability',
    harvestAr: 'متاحة للتوريد على مدار العام',
    packaging: '10 kg bulk export cartons / private label',
    temp: '-18°C or colder'
  },
  {
    id: 'french-fries',
    category: 'processed',
    nameEn: 'French fries',
    nameAr: 'بطاطس نصف مقلية',
    image: 'assets/images/prod_french_fries.jpg?v=20261104_v7',
    gallery: [
      'assets/images/prod_french_fries.jpg?v=20261104_v7',
      'assets/images/cat_processed.jpg?v=20261104_v7'
    ],
    stylesEn: 'Straight cut (Par-fried frozen)',
    stylesAr: 'تقطيع طولي مستقيم (نصف مقلية مجمدة)',
    sizesEn: 'Customer specifications / حسب مواصفات العميل',
    sizesAr: 'حسب مواصفات العميل / Customer specifications',
    harvestEn: 'Year-Round supply capability',
    harvestAr: 'متاحة للتوريد على مدار العام',
    packaging: 'Bulk catering 2.5 kg bags x 4 (10 kg carton)',
    temp: '-18°C or colder'
  },
  {
    id: 'falafel',
    category: 'processed',
    nameEn: 'Falafel (Taameya)',
    nameAr: 'فلافل / طعمية',
    image: 'assets/images/prod_falafel.jpg?v=20261104_v7',
    gallery: [
      'assets/images/prod_falafel.jpg?v=20261104_v7',
      'assets/images/cat_processed.jpg?v=20261104_v7'
    ],
    stylesEn: 'Balls',
    stylesAr: 'كرات (سادة أو بالسمسم)',
    sizesEn: 'Weight and diameter by agreement',
    sizesAr: 'الوزن والقطر طبقاً لطلب العميل',
    harvestEn: 'Year-Round supply capability',
    harvestAr: 'متاحة للتوريد على مدار العام',
    packaging: 'Catering boxes / Retail thermoformed packs',
    temp: '-18°C or colder'
  }
];

// 2. Bilingual Dictionary
const I18N = {
  en: {
    top_status: "Direct Export Sourcing Desk Active • Season 2026/2027",
    brand_subtitle: "Agricultural Crops & IQF Supply",
    nav_home: "Home",
    nav_about: "About Us",
    nav_products: "Products",
    nav_calendar: "Harvest Calendar",
    nav_quality: "Quality & Safety",
    nav_contact: "Contact Us",
    nav_review_btn: "Client Review",
    client_approval: "Client Review",
    nav_rfq_btn: "Export RFQ",

    hero_pill: "Egyptian IQF Food Processing & Export Heritage",
    hero_heading: "IQF PRODUCTS PORTFOLIO",
    hero_subline: "Seasonal Harvest Calendar • Product Forms • Quality Standards",
    hero_description: "An Egyptian food-processing company established in 1999 and founded by Dr. Mohamed Gabr. Delivering individually quick frozen (IQF) fruits, premium vegetables, and customized ready-to-cook products to world-class standards.",
    highlight_est: "Established Year",
    highlight_founder: "Founder & Owner",
    highlight_products: "Export Portfolio (26 Items)",
    highlight_temp: "Thermal Deep Freeze",
    btn_explore_products: "Explore Product Catalogue",
    btn_explore_text: "Explore Product Catalogue",
    btn_whatsapp_inquire: "WhatsApp Export Desk",
    btn_download_pdf: "Proposal PDF (Full Portfolio)",

    cat_section_badge: "PORTFOLIO SEGMENTS",
    cat_section_title: "Three Core Product Categories",
    cat_section_subtitle: "Crafted with precision cutting, strict cryogenic freezing, and customized packaging formats.",
    cat_fruits_title: "IQF Fruits",
    cat_fruits_desc: "Sweet, sun-ripened Egyptian fruits individually quick-frozen at harvest peak. Preserving aroma, cellular structure, and vibrant color.",
    cat_vegetables_title: "IQF Vegetables",
    cat_vegetables_desc: "Tender Egyptian vegetables harvested across the fertile Nile Delta, blanched, caliber-screened, and frozen immediately to retain nutrients.",
    cat_processed_title: "Processed & Ready-to-Cook",
    cat_processed_desc: "High-convenience commercial products including straight-cut French fries, customized vegetable blends, and authentic Egyptian falafel patties.",
    cat_view_btn: "View Product Specifications →",

    about_badge: "CORPORATE IDENTITY",
    about_title: "About GREEN ALEX",
    about_subtitle: "An established Egyptian food-processing leader founded on seasonal mastery and strict quality control.",
    cred_title: "Official Corporate Credentials & Registration",
    cred_item: "Item / Specification",
    cred_details: "Official Verified Details",

    nav_retail_brand: "Retail Brand (Virdi Va)",
    prod_badge: "TECHNICAL CATALOGUE",
    prod_title: "Our Product Portfolio (26 Items)",
    prod_subtitle: "Comprehensive IQF and ready-to-cook catalogue with available styles, cutting dimensions, and customized blends.",
    filter_all: "All Products (26)",
    filter_fruits: "IQF Fruits (5)",
    filter_vegetables: "IQF Vegetables (15)",
    filter_processed: "Mixed & Processed (6)",
    search_placeholder: "Search by name (e.g., Strawberry, بامية, Taro, Figs)...",
    note_heading: "Important Product Note (Official):",
    note_body: "Product forms and cutting sizes are common commercial options. Final specifications, grading, blend ratios and packaging requirements are agreed with each customer and confirmed through approved product specification sheets and samples.",
    note_body_ar: "أشكال التصنيع ومقاسات التقطيع المذكورة أعلاه هي خيارات تجارية شائعة. يتم الاتفاق على المواصفات النهائية ودرجات الفرز ونسب الخلط واشتراطات التعبئة مع كل عميل وتأكيدها عبر بطاقات مواصفات المنتج والعينات المعتمدة.",

    brand_badge: "APPROVED PACKAGING TRADEMARK",
    brand_title: "Virdi Va™ — Approved Retail Packaging Brand",
    retail_brand_subtitle: "GREEN ALEX's proprietary retail trademark for 400g consumer frozen pouches, alongside private-label packaging solutions for international retail chains.",
    brand_feat_1_title: "100% Natural Freshness",
    brand_feat_1_desc: "Selected crops frozen rapidly via IQF technology with zero chemical additives or artificial preservatives.",
    brand_feat_2_title: "Certified 400g Retail Pack",
    brand_feat_2_desc: "High-barrier printed pillow pouches engineered for premium supermarket shelf appeal and cold-chain protection.",
    brand_feat_3_title: "Core Retail Range",
    brand_feat_3_desc: "Green Beans (فاصوليا خضراء), Green Peas (بسلة خضراء), Diced Carrots (جزر مقطع), and Frozen Strawberries (فراولة مجمدة).",
    brand_feat_4_title: "Dual Export Capability",
    brand_feat_4_desc: "Available directly under the approved 'Virdi Va™' trademark or customized under Buyer's Private Label.",
    brand_wa_btn: "Inquire for Virdi Va™ Retail Distribution",

    nav_packaging: "Packaging Options",
    pkg_badge: "PACKAGING FORMATS & LOGISTICS",
    pkg_title: "PACKAGING OPTIONS | أوزان وطرق التعبئة",
    pkg_subtitle: "Available packaging formats and weights | أوزان وأشكال التعبئة المتاحة",
    pkg_type_retail: "Retail Pack • عبوة تجزئة",
    pkg_card_1_title: "Plastic Bags | أكياس",
    pkg_card_1_desc: "Consumer pillow pouches engineered for supermarket shelves, cold display cabinets, and private label packaging programs.",
    pkg_target_retail: "Supermarket & Retail Chains",
    pkg_type_catering: "Food Service • توريد فندقي",
    pkg_card_2_title: "Plastic Bags | أكياس",
    pkg_card_2_desc: "Institutional poly pouches crafted for Horeca, central kitchens, hotels, and food service operators requiring commercial culinary yield.",
    pkg_target_horeca: "Horeca & Commercial Kitchens",
    pkg_type_export: "Export Standard • كرتون تصدير",
    pkg_card_3_title: "Cartons | كراتين",
    pkg_card_3_desc: "5-ply corrugated master cartons with food-grade blue polyethylene liners, optimized for container sea freight and pallet stability.",
    pkg_target_export: "B2B Maritime & Reefer Export",
    pkg_type_bulk: "Industrial Bulk • توريد تصنيعي",
    pkg_card_4_title: "Woven Sacks | أجولة",
    pkg_card_4_desc: "High-strength woven polypropylene bags for industrial food manufacturers, puree/jam processors, and bulk repackers.",
    pkg_target_industrial: "Industrial Food Processing",
    pkg_table_title: "Official Packaging Matrix | جدول أوزان وأنظمة التعبئة الرسمية",
    pkg_col_type_en: "Packaging Type",
    pkg_col_type_ar: "نوع التعبئة",
    pkg_col_wt_en: "Weight",
    pkg_col_wt_ar: "الوزن",
    pkg_flex_title: "Packaging Flexibility | مرونة التعبئة",
    pkg_flex_badge: "Custom Client Specifications",
    pkg_flex_en: '"Available in different packaging options according to customer requirements and product specifications."',
    pkg_flex_ar: '"متاحة بأكثر من نظام تعبئة وفقاً لمتطلبات العملاء وطبيعة ومواصفات كل منتج."',
    pkg_cta_wa: "Inquire for Customized Packaging",

    cal_badge: "AGRICULTURAL CROP WINDOWS",
    cal_title: "Seasonal Harvest Calendar",
    cal_subtitle: "Synchronize export procurement contracts with Egyptian agricultural crop peak windows.",
    cal_notice_badge: "OFFICIAL CROP WINDOW NOTICE",
    cal_disclaimer_en: '"These are indicative Egyptian crop windows. Actual availability may vary by governorate, variety, weather conditions and farming schedule."',
    cal_disclaimer_ar: '"الفترات التالية استرشادية للمحاصيل المصرية، وقد تختلف مواعيد التوافر الفعلية وفقاً للمحافظة والصنف والظروف الجوية والبرنامج الزراعي."',
    cal_winter_title: "Winter Crops (المحاصيل الشتوية)",
    cal_winter_range: "October through April",
    cal_summer_title: "Summer Crops (المحاصيل الصيفية)",
    cal_summer_range: "April through December",
    cal_year_title: "Year-Round / Processed Items",
    cal_year_range: "Supplied throughout the year",
    cal_year_desc: "French fries and falafel may be produced or supplied throughout the year, subject to raw-material sourcing, production planning and customer demand.",
    cal_year_desc_ar: "البطاطس نصف المقلية والفلافل: متاحة على مدار العام وفقاً لتوافر الخامات وخطة الإنتاج واحتياجات العملاء.",
    cal_th_crop: "Crop Name (EN / AR)",
    cal_th_peak: "Indicative Peak Season",
    cal_th_forms: "Product Forms",

    qa_badge: "FOOD SAFETY & STANDARDS",
    qa_title: "Quality & Food Safety References",
    qa_subtitle: "Adhering to Egyptian EOS specifications, international Codex standards, and rigorous cold-chain protocols.",
    qa_tab_eos: "Egyptian Standards (EOS)",
    qa_tab_intl: "International References (Codex / ISO)",
    qa_tab_qc: "8-Point IQF QC Pipeline",
    eos_heading: "Egyptian Organization for Standardization & Quality (EOS)",
    eos_intro: "Key Egyptian national standards governing quick frozen fruits and vegetables:",
    intl_heading: "International Food Safety & Codex References",
    intl_intro: "Global benchmarks referenced for frozen food processing, composition, and labeling:",
    qc_heading: "Core IQF Quality Control Pipeline (8 Critical Control Points)",
    qc_intro: "End-to-end quality assurance executed across every production batch:",
    qa_disclaimer_title: "IMPORTANT REGULATORY COMPLIANCE DISCLAIMER (PRESERVED VERBATIM)",
    qa_disclaimer_en: '"Listing a standard in this portfolio does not by itself mean that GREEN ALEX is certified to that standard, nor that every listed standard applies to every product. Current official texts and mandatory status must be checked with EOS and the competent authority. Destination-market and customer specifications may impose additional requirements."',
    qa_disclaimer_ar: '"تنبيه: إدراج أي مواصفة في هذا الملف لا يعني حصول GREEN ALEX على شهادة مطابقة لها، ولا يعني انطباق كل مواصفة على جميع المنتجات. يجب الرجوع إلى النصوص الرسمية المحدثة والتحقق من حالة الإلزام ونطاق التطبيق لدى الهيئة المصرية للمواصفات والجهات المختصة، مع مراعاة متطلبات بلد الاستيراد والعملاء."',

    contact_badge: "COMMUNICATION & INQUIRIES",
    contact_title: "Contact GREEN ALEX",
    contact_subtitle: "Direct trade inquiries, contract procurement, specification requests, and instant WhatsApp export channel.",
    corp_heritage: "Established in 1999 • Founded by Dr. Mohamed Gabr",
    contact_admin_label: "Administration Office:",
    contact_reg_label: "Commercial Registration:",
    contact_founder_label: "Founder & Owner:",
    contact_wa_label: "Direct Mobile / WhatsApp Desk:",
    wa_active_note: "Available 24/7 for Global Importers",
    btn_dl_full_pdf: "Download Client Review PDF (Full Portfolio)",

    rfq_badge: "INSTANT B2B INQUIRY",
    rfq_title: "Build Your Export Specification RFQ",
    rfq_subtitle: "Select your desired product, volume, and specifications to generate an instant formatted WhatsApp dispatch.",
    form_product: "Product of Interest *",
    form_volume: "Estimated Volume *",
    form_packaging: "Packaging Format",
    form_destination: "Destination Port / Country *",
    form_buyer_name: "Your Name / Title *",
    form_buyer_company: "Company Name *",
    form_notes: "Specific Cutting Sizes or Requirements",
    form_submit_wa: "Send RFQ via WhatsApp to +20 109 300 3736",

    footer_summary: "Egyptian food-processing company established in 1999 and founded by Dr. Mohamed Gabr. Sourcing from prime Egyptian agricultural regions with full cold-chain integrity.",
    footer_links_title: "Portfolio Pages",
    footer_contact_title: "Administration & Contact"
  },

  ar: {
    top_status: "مكتب التصدير المباشر متاح للتعاقدات • موسم 2026/2027",
    brand_subtitle: "للحاصلات الزراعية ومنتجات التجميد السريع (IQF)",
    nav_home: "الرئيسية",
    nav_about: "نبذة عنا",
    nav_products: "منتجاتنا",
    nav_calendar: "تقويم الحصاد",
    nav_quality: "الجودة والسلامة",
    nav_contact: "اتصل بنا",
    nav_review_btn: "مراجعة العميل",
    client_approval: "مراجعة العميل",
    nav_rfq_btn: "طلب تسعير",

    hero_pill: "ريادة مصرية في تصنيع وتصدير الخضروات والفواكه المجمدة IQF",
    hero_heading: "بورتفوليو منتجات التجميد السريع IQF",
    hero_subline: "التقويم الموسمي للحصاد • أشكال التصنيع • معايير الجودة",
    hero_description: "شركة تصنيع غذائي مصرية تأسست عام 1999 على يد الدكتور/ محمد جبر. نختص في تصنيع وتوريد الفواكه والخضروات المجمدة بالتجميد الفردي السريع والمنتجات المجهزة للطهي بأعلى المعايير العالمية.",
    highlight_est: "سنة التأسيس",
    highlight_founder: "المؤسس والمالك",
    highlight_products: "محفظة التصدير (26 صنف)",
    highlight_temp: "التجميد العميق",
    btn_explore_products: "تصفح كتالوج المنتجات",
    btn_explore_text: "تصفح كتالوج المنتجات",
    btn_whatsapp_inquire: "مكتب التصدير عبر واتساب",
    btn_download_pdf: "ملف مراجعة الهيكل PDF (شامل الكتالوج)",

    nav_retail_brand: "العلامة التجارية (فيرديفا)",
    cat_section_badge: "قطاعات الإنتاج",
    cat_section_title: "ثلاث فئات أساسية للمنتجات",
    cat_section_subtitle: "تجهيز دقيق، تجميد فردي فائق السرعة، وخيارات تعبئة وتغليف مخصصة لأسواق التصدير.",
    cat_fruits_title: "الفواكه المجمدة IQF",
    cat_fruits_desc: "فواكه مصرية طبيعية مجمدة فردياً في ذروة النضج، تشمل الفراولة والمانجو وحبوب الرمان والتين والمشمش.",
    cat_vegetables_title: "الخضروات المجمدة IQF",
    cat_vegetables_desc: "خضروات الدلتا الطازجة (15 صنفاً تشمل البسلة، الفاصوليا، البامية درجات، القلقاس، البطاطا، البصل الأخضر وغيرها).",
    cat_processed_title: "الخضروات المشكلة والمصنعة",
    cat_processed_desc: "خلطات الخضار المشكلة بأنواعها الثنائية والثلاثية والرباعية والمخصصة، والبطاطس نصف المقلية، والفلافل.",
    cat_view_btn: "عرض مواصفات المنتجات ←",

    about_badge: "الهوية المؤسسية",
    about_title: "عن شركة GREEN ALEX",
    about_subtitle: "صرح مصري رائد في التصنيع الغذائي يعتمد التخطيط الموسمي والالتزام الصارم بمعايير الجودة.",
    cred_title: "بيانات الشركة المعتمدة والسجل التجاري",
    cred_item: "البيان / العنصر",
    cred_details: "التفاصيل الرسمية المعتمدة",

    prod_badge: "الكتالوج الفني",
    prod_title: "كتالوج المنتجات الكامل (26 صنف)",
    prod_subtitle: "دليل المواصفات الفنية لمنتجات التجميد السريع والخلطات المشكلة والجاهزة للطهي ومقاسات التقطيع المعتمدة.",
    filter_all: "كافة المنتجات (26)",
    filter_fruits: "الفواكه المجمدة (5)",
    filter_vegetables: "الخضروات المجمدة (15)",
    filter_processed: "الخضروات المشكلة والمصنعة (6)",
    search_placeholder: "ابحث باسم المنتج (مثال: فراولة، بامية، تين، قلقاس)...",
    note_heading: "ملاحظة هامة بشأن المنتجات (المعتمدة):",
    note_body: "أشكال التصنيع ومقاسات التقطيع المذكورة أعلاه هي خيارات تجارية شائعة. يتم الاتفاق على المواصفات النهائية ودرجات الفرز ونسب الخلط واشتراطات التعبئة والتغليف مع كل عميل وتأكيدها عبر بطاقات مواصفات المنتج والعينات المعتمدة.",
    note_body_ar: "أشكال التصنيع ومقاسات التقطيع المذكورة أعلاه هي خيارات تجارية شائعة. يتم الاتفاق على المواصفات النهائية ودرجات الفرز ونسب الخلط واشتراطات التعبئة والتغليف مع كل عميل وتأكيدها عبر بطاقات مواصفات المنتج والعينات المعتمدة.",

    brand_badge: "العلامة التجارية المعتمدة لتعبئة الأكياس",
    brand_title: "علامة فيرديفا (Virdi Va™) المعتمدة للتعبئة والتجزئة",
    retail_brand_subtitle: "العلامة التجارية الرسمية المعتمدة لشركة GREEN ALEX لتعبئة أكياس التجزئة زنة 400 جم للمستهلك النهائي، مع إمكانية التعبئة للغير (Private Label) لكبرى سلاسل السوبرماركت العالمية.",
    brand_feat_1_title: "منتجات طبيعية 100%",
    brand_feat_1_desc: "محاصيل منتقاة بعناية ومجمدة بالتجميد الفردي السريع IQF بدون أي إضافات كيميائية أو مواد حافظة.",
    brand_feat_2_title: "عبوات أكياس 400 جم معتمدة",
    brand_feat_2_desc: "أكياس تعبئة عالية الجودة مصممة للعرض في سلاسل السوبرماركت والتجزئة مع حماية كاملة لسلسلة التبريد.",
    brand_feat_3_title: "التشكيلة الأساسية المعبأة",
    brand_feat_3_desc: "فاصوليا خضراء، بسلة خضراء، جزر مكعبات، وفراولة مجمدة، إلى جانب البامية والملوخية والخلطات.",
    brand_feat_4_title: "خيارات التصدير والعلامات الخاصة",
    brand_feat_4_desc: "التوريد متاح بالعلامة التجارية المعتمدة Virdi Va™ أو بعلامة العميل التجارية الخاصة (Private Label).",
    brand_wa_btn: "طلب تسعير تعبئة وتوزيع فيرديفا Virdi Va™ عبر واتساب",

    nav_packaging: "أوزان وطرق التعبئة",
    pkg_badge: "خيارات ومواصفات التعبئة والتغليف",
    pkg_title: "أوزان وطرق التعبئة | PACKAGING OPTIONS",
    pkg_subtitle: "أوزان وأشكال التعبئة المتاحة | Available packaging formats and weights",
    pkg_type_retail: "عبوة تجزئة • Retail Pack",
    pkg_card_1_title: "أكياس بلاستيكية | Plastic Bags",
    pkg_card_1_desc: "أكياس للمستهلك وسلاسل السوبرماركت وثلاجات العرض، متاحة بعلامة فيرديفا (Virdi Va™) أو تحت العلامة التجارية الخاصة بالعميل (Private Label).",
    pkg_target_retail: "سلاسل السوبرماركت والتجزئة",
    pkg_type_catering: "توريد فندقي • Food Service",
    pkg_card_2_title: "أكياس بلاستيكية | Plastic Bags",
    pkg_card_2_desc: "أكياس مخصصة للمطابخ المركزية والفنادق والمطاعم وشركات الإعاشة لضمان أعلى إنتاجية وسهولة في الاستخدام الشيفاتي.",
    pkg_target_horeca: "قطاع هوريكا والمطابخ التجارية",
    pkg_type_export: "كرتون تصدير معتمد • Export Standard",
    pkg_card_3_title: "كراتين تصدير | Cartons",
    pkg_card_3_desc: "كراتين مضلعة قوية 5 طبقات مع بطانة بولي إيثيلين زرقاء مخصصة للأغذية، مصممة لتحمل الشحن البحري في الحاويات المبردة.",
    pkg_target_export: "التصدير البحري B2B والحاويات المبردة",
    pkg_type_bulk: "توريد تصنيعي ضخم • Industrial Bulk",
    pkg_card_4_title: "أجولة منسوجة | Woven Sacks",
    pkg_card_4_desc: "أجولة بولي بروبيلين منسوجة فائقة التحمل للمصانع الغذائية الكبرى ومصنعي المربيات والصلصات وشركات إعادة التعبئة.",
    pkg_target_industrial: "المصانع وخطوط الإنتاج الغذائي",
    pkg_table_title: "جدول أوزان وأنظمة التعبئة الرسمية المعتمدة",
    pkg_col_type_en: "Packaging Type (نوع التعبئة بالإنجليزية)",
    pkg_col_type_ar: "نوع التعبئة",
    pkg_col_wt_en: "Weight (الوزن بالإنجليزية)",
    pkg_col_wt_ar: "الوزن",
    pkg_flex_title: "مرونة التعبئة | Packaging Flexibility",
    pkg_flex_badge: "سياسة المرونة حسب رغبة العميل",
    pkg_flex_en: '"Available in different packaging options according to customer requirements and product specifications."',
    pkg_flex_ar: '"متاحة بأكثر من نظام تعبئة وفقاً لمتطلبات العملاء وطبيعة ومواصفات كل منتج."',
    pkg_cta_wa: "استفسر عن مواصفات التعبئة المخصصة عبر واتساب",

    cal_badge: "مواسم المحاصيل الزراعية",
    cal_title: "التقويم الموسمي للحصاد",
    cal_subtitle: "تنسيق خطط التوريد والشحن الدولي مع فترات ذروة جني المحاصيل الزراعية المصرية.",
    cal_notice_badge: "تنويه رسمي بشأن فترات الحصاد",
    cal_disclaimer_en: '"These are indicative Egyptian crop windows. Actual availability may vary by governorate, variety, weather conditions and farming schedule."',
    cal_disclaimer_ar: '"الفترات التالية استرشادية للمحاصيل المصرية، وقد تختلف مواعيد التوافر الفعلية وفقاً للمحافظة والصنف والظروف الجوية والبرنامج الزراعي."',
    cal_winter_title: "المحاصيل الشتوية",
    cal_winter_range: "من أكتوبر حتى أبريل",
    cal_summer_title: "المحاصيل الصيفية",
    cal_summer_range: "من أبريل حتى ديسمبر",
    cal_year_title: "منتجات متاحة على مدار العام",
    cal_year_range: "إمداد مستمر طوال السنة",
    cal_year_desc: "French fries and falafel may be produced or supplied throughout the year, subject to raw-material sourcing, production planning and customer demand.",
    cal_year_desc_ar: "البطاطس نصف المقلية والفلافل: متاحة على مدار العام وفقاً لتوافر الخامات وخطة الإنتاج واحتياجات العملاء.",
    cal_th_crop: "اسم المحصول (عربي / إنجليزي)",
    cal_th_peak: "موسم الذروة الاسترشادي",
    cal_th_forms: "أشكال التصنيع",

    qa_badge: "سلامة الغذاء والمواصفات",
    qa_title: "مراجع الجودة وسلامة الغذاء",
    qa_subtitle: "التزام كامل بالمواصفات القياسية المصرية EOS ومراجع الكودكس الدولية وضمان سلسلة التبريد.",
    qa_tab_eos: "المواصفات القياسية المصرية (EOS)",
    qa_tab_intl: "المراجع الدولية (Codex / ISO)",
    qa_tab_qc: "نقاط فحص الجودة (8 نقاط)",
    eos_heading: "الهيئة المصرية العامة للمواصفات والجودة (EOS)",
    eos_intro: "أهم المواصفات القياسية المصرية المنظمة لتصنيع وتداول الفواكه والخضروات المجمدة:",
    intl_heading: "المراجع والمواصفات الدولية وسلامة الغذاء",
    intl_intro: "المراجع والمعايير العالمية المعتمدة لخصائص التركيب وبطاقات البيانات والملوثات:",
    qc_heading: "منظومة فحص ومراقبة الجودة (8 مراحل حيوية)",
    qc_intro: "إجراءات رقابة الجودة المطبقة في كل خطوة إنتاجية لضمان سلامة المنتج:",
    qa_disclaimer_title: "تنبيه قانوني وتنظيمي هام (طبقاً للنص المعتمد)",
    qa_disclaimer_en: '"Listing a standard in this portfolio does not by itself mean that GREEN ALEX is certified to that standard, nor that every listed standard applies to every product. Current official texts and mandatory status must be checked with EOS and the competent authority. Destination-market and customer specifications may impose additional requirements."',
    qa_disclaimer_ar: '"تنبيه: إدراج أي مواصفة في هذا الملف لا يعني حصول GREEN ALEX على شهادة مطابقة لها، ولا يعني انطباق كل مواصفة على جميع المنتجات. يجب الرجوع إلى النصوص الرسمية المحدثة والتحقق من حالة الإلزام ونطاق التطبيق لدى الهيئة المصرية للمواصفات والجهات المختصة، مع مراعاة متطلبات بلد الاستيراد والعملاء."',

    contact_badge: "التواصل والتعاقدات",
    contact_title: "اتصل بشركة GREEN ALEX",
    contact_subtitle: "استفسارات التصدير، طلبات المواصفات والأسعار، والتواصل المباشر مع مكتب الإدارة عبر واتساب.",
    corp_heritage: "تأسست عام 1999 • المؤسس د. محمد جبر",
    contact_admin_label: "مقر الإدارة الرئيسي:",
    contact_reg_label: "السجل التجاري والإنتاج:",
    contact_founder_label: "المؤسس والمالك:",
    contact_wa_label: "مكتب التصدير والواتساب المباشر:",
    wa_active_note: "متاح على مدار الساعة للمستوردين والشركات الدولية",
    btn_dl_full_pdf: "تحميل ملف مراجعة الهيكل كاملاً PDF",

    rfq_badge: "طلب تسعير مباشر للتصدير",
    rfq_title: "إرسال طلب تسعير ومواصفات تجارية",
    rfq_subtitle: "اختر المنتج والكمية وميناء الوصول لتجهيز رسالة استفسار مهنية تُرسل فوراً عبر واتساب.",
    form_product: "المنتج المطلوب *",
    form_volume: "الكمية التقديرية *",
    form_packaging: "نمط التعبئة والتغليف",
    form_destination: "ميناء الوصول / الدولة *",
    form_buyer_name: "الاسم والمسمى الوظيفي *",
    form_buyer_company: "اسم الشركة / المؤسسة *",
    form_notes: "مقاسات تقطيع محددة أو اشتراطات خاصة",
    form_submit_wa: "إرسال طلب التسعير عبر واتساب (+20 109 300 3736)",

    footer_summary: "شركة مصرية للتصنيع الغذائي تأسست عام 1999 على يد د. محمد جبر. نعتمد التوريد من أخصب مزارع مصر مع ضمان كامل لسلسلة التبريد.",
    footer_links_title: "صفحات البورتفوليو",
    footer_contact_title: "الإدارة والتواصل"
  }
};

let currentLang = 'en';

// 3. Initialization
document.addEventListener('DOMContentLoaded', () => {
  renderProducts('all');
  initSearch();
  initLanguage();
  initScrollSpy();
  initMobileNav();
});

// 4. Render Products Function
function renderProducts(filter = 'all', searchQuery = '') {
  const grid = document.getElementById('productsGrid');
  if (!grid) return;

  const q = searchQuery.trim().toLowerCase();
  
  const filtered = PRODUCTS.filter(p => {
    const matchesCategory = (filter === 'all') || (p.category === filter);
    const matchesSearch = !q || 
      p.nameEn.toLowerCase().includes(q) || 
      p.nameAr.includes(q) || 
      p.stylesEn.toLowerCase().includes(q) || 
      p.stylesAr.includes(q);
    return matchesCategory && matchesSearch;
  });

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 50px 20px; color: #94a3b8;">
        <svg style="width: 48px; height: 48px; margin-bottom: 12px; color: #64748b;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        <p style="font-size: 1.1rem; font-weight: 700;">No products match your search query.</p>
        <p style="font-size: 0.88rem;">Try clearing the filter or searching for another crop.</p>
      </div>
    `;
    return;
  }

  grid.innerHTML = filtered.map(p => {
    const isAr = (currentLang === 'ar');
    const primaryName = isAr ? p.nameAr : p.nameEn;
    const secondaryName = isAr ? p.nameEn : p.nameAr;
    const styles = isAr ? p.stylesAr : p.stylesEn;
    const sizes = isAr ? p.sizesAr : p.sizesEn;
    const categoryLabel = p.category === 'fruits' ? (isAr ? 'فواكه IQF' : 'IQF Fruits')
      : p.category === 'vegetables' ? (isAr ? 'خضروات IQF' : 'IQF Vegetables')
      : (isAr ? 'مشكلة ومصنعة' : 'Mixed / Processed');

    const waText = encodeURIComponent(
      `Hello GREEN ALEX Export Team,\n\nI am inquiring about *${p.nameEn}* (${p.nameAr}).\n- Requested Forms: ${p.stylesEn}\n- Commercial Sizes: ${p.sizesEn}\n\nPlease share the official technical specification sheet and export quotation.`
    );

    return `
      <div class="product-card" data-category="${p.category}" data-product-id="${p.id}">
        <div class="prod-img-wrap">
          <img src="${p.image}" alt="${p.nameEn}" loading="lazy">
          <span class="prod-category-badge">${categoryLabel}</span>
        </div>
        
        <div class="prod-info">
          <div class="prod-names">
            <span class="prod-name-en">${primaryName}</span>
            <span class="prod-name-ar">${secondaryName}</span>
          </div>

          <div class="prod-meta-row">
            <span class="meta-label">${isAr ? 'أشكال التصنيع:' : 'Styles:'}</span>
            <span class="meta-val">${styles}</span>
          </div>

          <div class="prod-sizes-box">
            <span class="meta-label">${isAr ? 'المقاسات:' : 'Sizes:'}</span>
            <span class="sizes-highlight">${sizes}</span>
          </div>

          <div class="prod-actions">
            <a href="https://wa.me/201093003736?text=${waText}" target="_blank" class="prod-btn-wa" title="Quick Inquiry via WhatsApp">
              <svg class="icon-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
              <span>${isAr ? 'واتساب' : 'Inquire'}</span>
            </a>
            <button class="prod-btn-spec" onclick="openProductModal('${p.id}')">
              ${isAr ? 'المواصفات' : 'Full Specs'}
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// 5. Filter Category Handler
function filterCategory(category) {
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-filter') === category);
  });
  
  const searchInput = document.getElementById('productSearch');
  const q = searchInput ? searchInput.value : '';
  renderProducts(category, q);
}

// 6. Search Input Handler
function initSearch() {
  const searchInput = document.getElementById('productSearch');
  if (!searchInput) return;

  searchInput.addEventListener('input', (e) => {
    const activeBtn = document.querySelector('.filter-btn.active');
    const category = activeBtn ? activeBtn.getAttribute('data-filter') : 'all';
    renderProducts(category, e.target.value);
  });
}

// 7. Product Detail Modal with Multi-Image Gallery Support
function openProductModal(productId) {
  const p = PRODUCTS.find(item => item.id === productId);
  if (!p) return;

  const isAr = (currentLang === 'ar');
  const modal = document.getElementById('productModal');
  const content = document.getElementById('productModalContent');

  // Support multiple images per product
  const images = p.gallery && p.gallery.length ? p.gallery : (p.images || [p.image]);
  const primaryImg = images[0];

  const waText = encodeURIComponent(
    `Hello GREEN ALEX Export Desk,\n\nI am requesting full technical specifications, packing options, and container load pricing for:\nProduct: ${p.nameEn} (${p.nameAr})\nStyle: ${p.stylesEn}\nCutting Size: ${p.sizesEn}\n\nThank you.`
  );

  const galleryHtml = images.length > 1 ? `
    <div class="modal-gallery-thumbs" style="display: flex; gap: 8px; margin-top: 10px;">
      ${images.map((img, idx) => `
        <img src="${img}" alt="${p.nameEn} view ${idx+1}" 
          class="gallery-thumb ${idx === 0 ? 'active' : ''}" 
          style="width: 55px; height: 55px; border-radius: 6px; object-fit: cover; cursor: pointer; border: 2px solid ${idx === 0 ? 'var(--gold-400)' : 'rgba(255,255,255,0.1)'}; transition: all 0.2s;"
          onclick="switchModalImage(this, '${img}')">
      `).join('')}
    </div>
  ` : '';

  content.innerHTML = `
    <div style="display: flex; gap: 20px; align-items: flex-start; margin-bottom: 20px; flex-wrap: wrap;">
      <div style="display: flex; flex-direction: column; align-items: center;">
        <img id="modalMainImg" src="${primaryImg}" alt="${p.nameEn}" style="width: 140px; height: 140px; border-radius: 12px; object-fit: cover; border: 2px solid var(--emerald-500); box-shadow: 0 4px 15px rgba(0,0,0,0.4);">
        ${galleryHtml}
      </div>
      <div style="flex: 1; min-width: 220px;">
        <span class="modal-badge">${p.category.toUpperCase()}</span>
        <h3 style="font-size: 1.6rem; color: #ffffff; margin-bottom: 4px;">${p.nameEn} <span style="font-family: var(--font-ar); color: var(--gold-400);">(${p.nameAr})</span></h3>
        <p style="font-size: 0.88rem; color: var(--emerald-400); font-weight: 600;">Standard Thermal Cold Chain: ${p.temp}</p>
        ${images.length > 1 ? `<span style="display: inline-block; font-size: 0.75rem; background: rgba(212,175,55,0.15); color: var(--gold-300); padding: 2px 8px; border-radius: 4px; margin-top: 6px;">📷 ${images.length} ${isAr ? 'صور متاحة' : 'Product Photos'}</span>` : ''}
      </div>
    </div>

    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 16px; margin-bottom: 20px;">
      <div style="margin-bottom: 10px;">
        <strong style="color: var(--slate-300); font-size: 0.85rem;">${isAr ? 'أشكال التصنيع المتاحة:' : 'Available Commercial Styles:'}</strong>
        <p style="color: #ffffff; font-size: 0.95rem; margin-top: 2px;">${isAr ? p.stylesAr : p.stylesEn}</p>
      </div>
      <div style="margin-bottom: 10px;">
        <strong style="color: var(--slate-300); font-size: 0.85rem;">${isAr ? 'المقاسات ودرجات الفرز:' : 'Dimensions & Screened Calibers:'}</strong>
        <p style="color: var(--gold-300); font-size: 0.95rem; font-weight: 700; margin-top: 2px;">${isAr ? p.sizesAr : p.sizesEn}</p>
      </div>
      <div style="margin-bottom: 10px;">
        <strong style="color: var(--slate-300); font-size: 0.85rem;">${isAr ? 'موسم الحصاد التقديري:' : 'Indicative Peak Harvest Season:'}</strong>
        <p style="color: #ffffff; font-size: 0.95rem; margin-top: 2px;">${isAr ? p.harvestAr : p.harvestEn}</p>
      </div>
      <div>
        <strong style="color: var(--slate-300); font-size: 0.85rem;">${isAr ? 'خيارات التعبئة والتغليف المعتادة:' : 'Common Packaging Formats:'}</strong>
        <p style="color: #cbd5e1; font-size: 0.9rem; margin-top: 2px;">${p.packaging}</p>
      </div>
    </div>

    <div style="background: rgba(212, 175, 55, 0.08); border-left: 3px solid var(--gold-500); padding: 10px 14px; border-radius: 4px; font-size: 0.82rem; color: #fef08a; margin-bottom: 20px;">
      ${isAr ? 'المواصفات النهائية ودرجات الفرز ونسب الخلط واشتراطات التعبئة والتغليف تؤكد رسمياً مع كل عميل عبر بطاقات المواصفات الفنية المعتمدة والعينات.' : 'Final specifications, grading, blend ratios and packaging requirements are agreed with each customer and confirmed through approved product specification sheets and samples.'}
    </div>

    <div style="display: flex; gap: 12px;">
      <a href="https://wa.me/201093003736?text=${waText}" target="_blank" class="btn btn-full btn-emerald">
        <svg class="icon-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
        <span>${isAr ? 'طلب تسعير لهذا الصنف عبر واتساب' : 'Request Pricing via WhatsApp'}</span>
      </a>
    </div>
  `;

  modal.classList.add('active');
}

// Function to switch active image in modal gallery
function switchModalImage(thumbEl, newSrc) {
  const mainImg = document.getElementById('modalMainImg');
  if (mainImg) mainImg.src = newSrc;
  document.querySelectorAll('.gallery-thumb').forEach(el => {
    el.classList.remove('active');
    el.style.borderColor = 'rgba(255,255,255,0.1)';
  });
  thumbEl.classList.add('active');
  thumbEl.style.borderColor = 'var(--gold-400)';
}

function closeProductModal(e) {
  const modal = document.getElementById('productModal');
  if (modal) modal.classList.remove('active');
}

// 8. Client Review Modal
function initReviewModal() {
  const btn = document.getElementById('reviewModalBtn');
  const modal = document.getElementById('reviewModal');
  if (btn && modal) {
    btn.addEventListener('click', () => modal.classList.add('active'));
  }
}
function closeReviewModal() {
  const modal = document.getElementById('reviewModal');
  if (modal) modal.classList.remove('active');
}

// 9. QA Tabs Switcher
function switchQaTab(tabId) {
  document.querySelectorAll('.qa-tab-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-tab') === tabId);
  });
  document.querySelectorAll('.qa-panel').forEach(panel => {
    panel.classList.toggle('active', panel.id === `tab-${tabId}`);
  });
}

// 10. WhatsApp RFQ Form Handler
function handleRfqSubmit(event) {
  event.preventDefault();
  
  const product = document.getElementById('rfqProduct').value;
  const volume = document.getElementById('rfqVolume').value;
  const packaging = document.getElementById('rfqPackaging').value;
  const destination = document.getElementById('rfqDestination').value;
  const buyerName = document.getElementById('buyerName').value;
  const buyerCompany = document.getElementById('buyerCompany').value;
  const notes = document.getElementById('rfqNotes').value;

  const msg = 
`*NEW COMMERCIAL EXPORT INQUIRY — GREEN ALEX*
----------------------------------------
*Product:* ${product}
*Estimated Volume:* ${volume}
*Packaging Format:* ${packaging}
*Destination Port/Country:* ${destination}
----------------------------------------
*Buyer Name:* ${buyerName}
*Company:* ${buyerCompany}
${notes ? `*Special Requirements:* ${notes}\n` : ''}----------------------------------------
Please provide current FOB/CIF pricing and export specification sheet.`;

  const waUrl = `https://wa.me/201093003736?text=${encodeURIComponent(msg)}`;
  window.open(waUrl, '_blank');
}

// 11. Bilingual Language Switcher
function initLanguage() {
  const btn = document.getElementById('langToggleBtn');
  const btnText = document.getElementById('langBtnText');
  const badge = btn ? btn.querySelector('.lang-badge') : null;

  initReviewModal();

  if (!btn) return;

  btn.addEventListener('click', () => {
    currentLang = (currentLang === 'en') ? 'ar' : 'en';
    applyLanguage(currentLang);
  });
}

function applyLanguage(lang) {
  document.documentElement.lang = lang;
  document.documentElement.dir = (lang === 'ar') ? 'rtl' : 'ltr';

  const btnText = document.getElementById('langBtnText');
  const badge = document.querySelector('.lang-badge');
  if (btnText) btnText.textContent = (lang === 'en') ? 'العربية' : 'English';
  if (badge) badge.textContent = (lang === 'en') ? 'AR' : 'EN';

  // Translate all elements with data-i18n
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (I18N[lang] && I18N[lang][key]) {
      el.textContent = I18N[lang][key];
    }
  });

  // Translate placeholders
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    if (I18N[lang] && I18N[lang][key]) {
      el.placeholder = I18N[lang][key];
    }
  });

  // Re-render products to match primary language
  const activeBtn = document.querySelector('.filter-btn.active');
  const category = activeBtn ? activeBtn.getAttribute('data-filter') : 'all';
  const searchInput = document.getElementById('productSearch');
  const q = searchInput ? searchInput.value : '';
  renderProducts(category, q);
}

// 12. Active Scroll Spy & Navigation Links
function initScrollSpy() {
  const sections = document.querySelectorAll('section[id]');
  const navItems = document.querySelectorAll('.nav-item');

  window.addEventListener('scroll', () => {
    let scrollY = window.pageYOffset;
    
    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 120;
      const sectionId = current.getAttribute('id');

      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        navItems.forEach(item => {
          item.classList.toggle('active', item.getAttribute('data-nav') === sectionId);
        });
      }
    });
  });
}

// 13. Mobile Navigation Menu Toggle
function initMobileNav() {
  const toggle = document.getElementById('mobileToggle');
  const menu = document.getElementById('navMenu');
  if (!toggle || !menu) return;

  toggle.addEventListener('click', () => {
    menu.classList.toggle('open');
  });

  document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
      menu.classList.remove('open');
    });
  });
}
