#!/usr/bin/env python3
"""Generate the saudicoffee.xyz multi-page trilingual site."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# TRANSLATIONS — all content in EN / ZH / AR
# ============================================================
T = {
  "common": {
    "logo": {"en": "PIF × NAPELL", "zh": "PIF × NAPELL", "ar": "PIF × NAPELL"},
    "nav_summary": {"en": "Summary", "zh": "摘要", "ar": "الملخص"},
    "nav_context": {"en": "Context", "zh": "背景", "ar": "السياق"},
    "nav_technology": {"en": "Technology", "zh": "技术", "ar": "التقنية"},
    "nav_market": {"en": "Market", "zh": "市场", "ar": "السوق"},
    "nav_proposal": {"en": "Proposal", "zh": "提案", "ar": "العرض"},
    "nav_roadmap": {"en": "Roadmap", "zh": "路线图", "ar": "خارطة الطريق"},
    "nav_financials": {"en": "Financials", "zh": "财务", "ar": "المالية"},
    "nav_risks": {"en": "Risks", "zh": "风险", "ar": "المخاطر"},
    "nav_alignment": {"en": "Alignment", "zh": "战略对齐", "ar": "التوافق"},
    "nav_blueprints": {"en": "Blueprints", "zh": "蓝图", "ar": "المخططات"},
    "nav_drawings": {"en": "Drawings", "zh": "图纸", "ar": "الرسومات"},
    "nav_video": {"en": "El Niño", "zh": "厄尔尼诺", "ar": "ظاهرة النينو"},
    "nav_connect": {"en": "Connect", "zh": "联系", "ar": "تواصل"},
    # Dropdowns
    "dd_summary_exec": {"en": "Executive Summary", "zh": "执行摘要", "ar": "الملخص التنفيذي"},
    "dd_summary_metrics": {"en": "Key Market Metrics", "zh": "关键市场指标", "ar": "مؤشرات السوق الرئيسية"},
    "dd_context_vision": {"en": "Vision 2030 Mandate", "zh": "愿景2030使命", "ar": "تفويض رؤية 2030"},
    "dd_context_import": {"en": "Market Import Volume", "zh": "市场进口量", "ar": "حجم استيراد السوق"},
    "dd_context_water": {"en": "Water Scarcity Crisis", "zh": "水资源危机", "ar": "أزمة ندرة المياه"},
    "dd_tech_patent": {"en": "Patent CN 202611094298.6", "zh": "专利 CN 202611094298.6", "ar": "براءة الاختراع CN 202611094298.6"},
    "dd_tech_robotic": {"en": "AI Robotic Tissue Culture", "zh": "AI机器人组培", "ar": "زراعة الأنسجة بالروبوت"},
    "dd_tech_aeroponic": {"en": "Atomization Hydroponics", "zh": "雾化水培系统", "ar": "نظام الزراعة الضبابية"},
    "dd_market_size": {"en": "Market Size & Growth", "zh": "市场规模与增长", "ar": "حجم السوق والنمو"},
    "dd_market_sub": {"en": "Import Substitution", "zh": "进口替代", "ar": "استبدال الاستيراد"},
    "dd_market_charts": {"en": "Growth Charts", "zh": "增长图表", "ar": "رسومات النمو"},
    "dd_prop_pif": {"en": "PIF Contribution", "zh": "PIF贡献", "ar": "مساهمة صندوق الاستثمارات"},
    "dd_prop_napell": {"en": "Napell Contribution", "zh": "Napell贡献", "ar": "مساهمة Napell"},
    "dd_prop_jv": {"en": "JV Structure", "zh": "合资结构", "ar": "هيكل المشروع المشترك"},
    "dd_road_1": {"en": "Phase 1: Pilot Farm", "zh": "阶段一：试验农场", "ar": "المرحلة 1: مزرعة تجريبية"},
    "dd_road_2": {"en": "Phase 2: Commercial Scale", "zh": "阶段二：商业规模", "ar": "المرحلة 2: نطاق تجاري"},
    "dd_road_3": {"en": "Phase 3: National Scale", "zh": "阶段三：全国规模", "ar": "المرحلة 3: نطاق وطني"},
    "dd_road_4": {"en": "Phase 4: Global Brand", "zh": "阶段四：全球品牌", "ar": "المرحلة 4: علامة عالمية"},
    "dd_fin_invest": {"en": "Investment Allocation", "zh": "投资分配", "ar": "توزيع الاستثمار"},
    "dd_fin_pl": {"en": "P&L Summary", "zh": "损益摘要", "ar": "ملخص الأرباح والخسائر"},
    "dd_fin_roi": {"en": "ROI Metrics", "zh": "投资回报指标", "ar": "مؤشرات العائد"},
    "dd_bp_robotic": {"en": "Robotic Arm Blueprint", "zh": "机械臂蓝图", "ar": "مخطط الذراع الروبوتي"},
    "dd_bp_aeroponic": {"en": "Aeroponic System Blueprint", "zh": "雾化系统蓝图", "ar": "مخطط نظام الضبوب"},
    "dd_drawings_system": {"en": "System Architecture", "zh": "系统架构", "ar": "بنية النظام"},
    "dd_drawings_facility": {"en": "Facility Layout", "zh": "设施布局", "ar": "تخطيط المنشأة"},
    "dd_video_crisis": {"en": "El Niño 2026 Coffee Crisis", "zh": "2026厄尔尼诺咖啡危机", "ar": "أزمة قهوة إلنينو 2026"},
    "dd_video_solution": {"en": "Aeroponic Solution", "zh": "气雾栽培解决方案", "ar": "حل الضبوب"},
    # Footer
    "footer_rights": {"en": "Napell Biotech (Hong Kong) Ltd. — All Rights Reserved.", "zh": "Napell Biotech (Hong Kong) Ltd. — 版权所有。", "ar": "Napell Biotech (Hong Kong) Ltd. — جميع الحقوق محفوظة."},
    "footer_patent": {"en": "Patent: CN 202611094298.6 — Gas-Liquid Atomization Based Full-Cycle Planting Management Method & System", "zh": "专利: CN 202611094298.6 — 基于气液式雾化的全周期种植管理方法及系统", "ar": "براءة الاختراع: CN 202611094298.6 — طريقة ونظام إدارة الزراعة طوال الدورة بناءً على الضبوب بالغاز والسائل"},
    "footer_confidential": {"en": "This document is confidential and intended solely for the Public Investment Fund (PIF) of the Kingdom of Saudi Arabia.", "zh": "本文件为机密文件，仅供沙特阿拉伯王国公共投资基金（PIF）使用。", "ar": "هذه الوثيقة سرية ومخصصة حصرياً لصندوق الاستثمارات العامة (PIF) للمملكة العربية السعودية."},
  },

  "index": {
    "confidential": {"en": "Confidential — For PIF Review Only", "zh": "机密 — 仅供PIF审阅", "ar": "سري — لمراجعة صندوق الاستثمارات العامة فقط"},
    "title": {"en": "Building Saudi Arabia's<br>Sovereign Coffee Industry Chain", "zh": "建设沙特阿拉伯<br>主权咖啡产业链", "ar": "بناء سلسلة صناعة القهوة<br>السيادية للمملكة العربية السعودية"},
    "subtitle": {"en": "A strategic partnership proposal leveraging proprietary AI-robotic tissue culture and gas-liquid atomization hydroponic technology to establish a fully integrated, climate-resilient coffee production ecosystem in the Kingdom of Saudi Arabia.", "zh": "一项战略合作提案，利用专利AI机器人组培技术和气液式雾化水培技术，在沙特阿拉伯王国建立完全集成的、气候适应性咖啡生产生态系统。", "ar": "عرض شراكة استراتيجية يستفيد من تقنية زراعة الأنسجة بالروبوت المدعوم بالذكاء الاصطناعي وتقنية الزراعة المائية الضبابية المسجلة لإنشاء نظام إنتاج قهوة متكامل ومقاوم للمناخ في المملكة العربية السعودية."},
    "meta_prepared": {"en": "Prepared by: Napell Biotech (Hong Kong) Ltd.", "zh": "编制方：Napell Biotech (Hong Kong) Ltd.", "ar": "أعد بواسطة: Napell Biotech (Hong Kong) Ltd."},
    "meta_date": {"en": "Date: July 2026", "zh": "日期：2026年7月", "ar": "التاريخ: يوليو 2026"},
    "meta_ref": {"en": "Ref: Patent CN 202611094298.6", "zh": "参考：专利 CN 202611094298.6", "ar": "المرجع: براءة الاختراع CN 202611094298.6"},
    "sec_num": {"en": "Section 01", "zh": "第 01 节", "ar": "القسم 01"},
    "sec_title": {"en": "Executive Summary", "zh": "执行摘要", "ar": "الملخص التنفيذي"},
    "sec_desc": {"en": "The opportunity, the technology, and why PIF should act now.", "zh": "机遇、技术和PIF为何应立即行动。", "ar": "الفرصة والتقنية ولماذا يجب على صندوق الاستثمارات العامة التحرك الآن."},
    "m1_val": {"en": "$900B+", "zh": "$900B+", "ar": "+$900B"},
    "m1_lbl": {"en": "PIF Assets Under Management (2026)", "zh": "PIF管理资产（2026）", "ar": "أصول صندوق الاستثمارات تحت الإدارة (2026)"},
    "m2_val": {"en": "SAR 5-7B", "zh": "SAR 50-70亿", "ar": "5-7B ريال"},
    "m2_lbl": {"en": "Saudi Coffee Market Value (2024)", "zh": "沙特咖啡市场价值（2024）", "ar": "قيمة سوق القهوة السعودي (2024)"},
    "m3_val": {"en": "80,000+", "zh": "80,000+", "ar": "+80,000"},
    "m3_lbl": {"en": "Tons Coffee Consumed Annually (Saudi)", "zh": "沙特年咖啡消费量（吨）", "ar": "طن قهوة مستهلكة سنوياً (السعودية)"},
    "m4_val": {"en": "~96%", "zh": "~96%", "ar": "~96%"},
    "m4_lbl": {"en": "Import Dependency Rate", "zh": "进口依赖率", "ar": "معدل الاعتماد على الاستيراد"},
    "p1": {"en": "Saudi Arabia is one of the world's largest coffee consumers — yet imports nearly all of its coffee beans. The Kingdom imports approximately <strong>188,000 tons</strong> of coffee annually (2024), spending over <strong>$400 million</strong> at an accelerating rate. Meanwhile, Saudi Arabia's scarce renewable water resources (2.4 billion m³/year — among the lowest per capita globally) make traditional open-field coffee cultivation environmentally impossible in most of the country.", "zh": "沙特阿拉伯是全球最大的咖啡消费国之一，却几乎进口所有咖啡豆。沙特每年进口约<strong>188,000吨</strong>咖啡（2024年），支出超过<strong>4亿美元</strong>且增速加快。与此同时，沙特可再生水资源极为稀缺（24亿立方米/年，人均全球最低之一），使传统露天咖啡种植在大部分地区环境上不可行。", "ar": "تعد السعودية من أكبر مستهلكي القهوة في العالم — لكنها تستورد تقريباً جميع حبوب القهوة. تستورد المملكة حوالي <strong>188,000 طن</strong> من القهوة سنوياً (2024)، تنفق أكثر من <strong>400 مليون دولار</strong> بمعدل متسارع. في غضون ذلك، الموارد المائية المتجددة المحدودة في السعودية (2.4 مليار م³/سنة — من بين الأدنى عالمياً نصيب الفرد) تجعل زراعة القهوة التقليدية في الحقول المفتوحة مستحيلة بيئياً في معظم أنحاء البلاد."},
    "p2": {"en": "<strong>Napell Biotech</strong> and <strong>Guangzhou Herang Modern Agriculture Technology</strong> have developed and patented (CN 202611094298.6) a breakthrough <strong>gas-liquid atomization full-cycle planting management system</strong>, integrated with <strong>AI-driven robotic tissue culture</strong> — a technology suite that enables coffee cultivation in controlled environments with <strong>90% less water</strong>, <strong>15× higher yield per m²</strong>, and <strong>first harvest in 12-14 months</strong> (vs. 3-4 years).", "zh": "<strong>Napell Biotech</strong>和<strong>广州禾穰现代农业科技有限公司</strong>已开发并申请专利（CN 202611094298.6）突破性的<strong>气液式雾化全周期种植管理系统</strong>，集成<strong>AI驱动的机器人组培技术</strong>——一套技术体系，可在受控环境中种植咖啡，<strong>节水90%</strong>、<strong>每平方米产量提高15倍</strong>、<strong>12-14个月内首次收获</strong>（对比传统3-4年）。", "ar": "قامت <strong>Napell Biotech</strong> و<strong>شركة قوانغتشو هيرانغ للتقنية الزراعية الحديثة</strong> بتطوير وتسجيل براءة اختراع (CN 202611094298.6) لـ<strong>نظام إدارة الزراعة طوال الدورة بالضبوب بالغاز والسائل</strong>، متكامل مع <strong>زراعة الأنسجة بالروبوت المدعوم بالذكاء الاصطناعي</strong> — مجموعة تقنية تتيح زراعة القهوة في بيئات محكومة بـ<strong>90% مياه أقل</strong>، <strong>إنتاجية أعلى 15 مرة لكل م²</strong>، و<strong>أول حصاد في 14-12 شهر</strong> (مقابل 3-4 سنوات)."},
    "p3": {"en": "This proposal outlines a <strong>$200-250M joint venture</strong> for PIF to establish, in partnership with Napell, a sovereign coffee industry chain — from AI-propelled tissue culture labs to vertical atomization farms to processing, roasting, and \"Saudi Origin\" branded retail — fully aligned with Vision 2030's food security, economic diversification, and technology transfer mandates. The JV targets <strong>5-8% import substitution by Year 7</strong> and <strong>15% by Year 10</strong>, generating <strong>$86-139M annual revenue</strong> by Year 5.", "zh": "本提案概述了一项<strong>2-2.5亿美元合资企业</strong>，供PIF与Napell合作建立主权咖啡产业链——从AI驱动的组培实验室到垂直雾化农场再到加工、烘焙和\"沙特原产地\"品牌零售——完全契合愿景2030的粮食安全、经济多元化和技术转移使命。合资企业目标<strong>第7年实现5-8%进口替代</strong>，<strong>第10年达15%</strong>，<strong>第5年产生8,600-13,900万美元年收入</strong>。", "ar": "يحدد هذا العرض <strong>مشروعاً مشتركاً بقيمة 200-250 مليون دولار</strong> لصندوق الاستثمارات العامة لإنشاء، بالشراكة مع Napell، سلسلة صناعة قهوة سيادية — من مختبرات زراعة الأنسجة بالروبوت إلى مزارع الضبوب العمودية إلى المعالجة والتحميص وتجارة التجزئة بعلامة \"المنشأ السعودي\" — متوافقاً تماماً مع تفويضات رؤية 2030 للأمن الغذائي والتنويع الاقتصادي ونقل التقنية. يستهدف المشروع المشترك <strong>5-8% استبدال استيراد بحلول السنة 7</strong> و<strong>15% بحلول السنة 10</strong>، محققاً <strong>86-139 مليون دولار إيرادات سنوية</strong> بحلول السنة 5."},
  },

  "context": {
    "sec_num": {"en": "Section 02", "zh": "第 02 节", "ar": "القسم 02"},
    "sec_title": {"en": "Strategic Context", "zh": "战略背景", "ar": "السياق الاستراتيجي"},
    "sec_desc": {"en": "Why Saudi Arabia needs sovereign coffee production — and why now.", "zh": "为何沙特阿拉伯需要主权咖啡生产——以及为何是现在。", "ar": "لماذا تحتاج المملكة العربية السعودية إلى إنتاج قهوة سيادي — ولماذا الآن."},
    "c1_title": {"en": "Vision 2030 Mandate", "zh": "愿景2030使命", "ar": "تفويض رؤية 2030"},
    "c1_text": {"en": "Saudi Arabia imports ~80% of its food. Vision 2030's National Food Security Program explicitly targets import dependency reduction through domestic production, agritech investment, and controlled environment agriculture. PIF's own Saudi Coffee Company was established in 2022 with a SAR 1.2 billion mandate to build a national coffee industry. Coffee is one of the few high-value crops where Saudi Arabia has significant domestic demand AND the cultural heritage to build a global brand.", "zh": "沙特进口约80%的食品。愿景2030的国家粮食安全计划明确目标通过国内生产、农业科技投资和受控环境农业降低进口依赖。PIF旗下的Saudi Coffee Company于2022年成立，获得12亿沙特里亚尔授权建设国家咖啡产业。咖啡是沙特拥有巨大国内需求且有文化遗产打造全球品牌的少数高价值作物之一。", "ar": "تستورد السعودية حوالي 80% من غذائها. يستهدف برنامج الأمن الغذائي الوطني في رؤية 2030 صراحةً تقليل الاعتماد على الاستيراد عبر الإنتاج المحلي والاستثمار في التقنية الزراعية والزراعة في البيئات المحكومة. تأسست شركة القهوة السعودية التابعة لصندوق الاستثمارات العامة في 2022 بتفويض 1.2 مليار ريال لبناء صناعة قهوة وطنية. القهوة هي واحدة من المحاصيل عالية القيمة القليلة التي تمتلك فيها السعودية طلباً محلياً كبيراً وتراثاً ثقافياً لبناء علامة عالمية."},
    "c2_title": {"en": "Market Import Volume", "zh": "市场进口量", "ar": "حجم استيراد السوق"},
    "c2_text": {"en": "Saudi Arabia imported <strong>188,000 tons of coffee beans in 2024</strong> with value growth of 21.3% YoY. In H1 2025 alone, imports surged to $315.77M — a 52.27% value increase driven by record global prices. Saudi Arabia pays a median import price of <strong>$8,612/ton</strong> vs. the global median of $4,657/ton — a reflection of the Kingdom's transition into a premium coffee destination. Domestic production is negligible at ~1,485 tons (2023), covering less than 2% of consumption.", "zh": "沙特2024年进口<strong>188,000吨咖啡豆</strong>，价值同比增长21.3%。仅2025年上半年，进口激增至3.1577亿美元——价值增长52.27%，受全球创纪录价格推动。沙特进口中位价为<strong>8,612美元/吨</strong>，而全球中位价为4,657美元/吨——反映了沙特向高端咖啡目的地的转型。国内产量微乎其微，约1,485吨（2023年），仅覆盖不到2%的消费量。", "ar": "استوردت السعودية <strong>188,000 طن من حبوب القهوة في 2024</strong> بنمو قيمة 21.3% سنوياً. في النصف الأول من 2025 وحده، ارتفعت الواردات إلى 315.77 مليون دولار — زيادة قيمة 52.27% مدفوعة بأسعار عالمية قياسية. تدفع السعودية سعر استيراد متوسط <strong>8,612 دولار/طن</strong> مقابل المتوسط العالمي 4,657 دولار/طن — انعكاس لتحول المملكة إلى وجهة قهوة متميزة. الإنتاج المحلي ضئيل عند حوالي 1,485 طن (2023)، يغطي أقل من 2% من الاستهلاك."},
    "c3_title": {"en": "Water Scarcity Crisis", "zh": "水资源危机", "ar": "أزمة ندرة المياه"},
    "c3_text": {"en": "Saudi Arabia's renewable water resources are among the lowest per capita globally. Traditional agriculture consumes 85% of national water use. The 2008 decision to phase out domestic wheat production due to aquifer depletion set a clear precedent: water-intensive open-field agriculture is not viable. This makes controlled environment agriculture (CEA) — not a choice, but a <strong>strategic necessity</strong> for any new agricultural initiative in the Kingdom.", "zh": "沙特可再生水资源人均全球最低之一。传统农业消耗全国85%的用水。2008年因含水层枯竭而逐步淘汰国内小麦生产的决定树立了明确先例：高耗水的露天农业不可行。这使得受控环境农业（CEA）不是一种选择，而是王国任何新农业倡议的<strong>战略必然</strong>。", "ar": "موارد المياه المتجددة في السعودية من بين الأدنى نصيب الفرد عالمياً. يستهلك الزراعة التقليدية 85% من استخدام المياه الوطني. قرار 2008 التدريجي للتخلص من إنتاج القمح المحلي بسبب استنزاف طبقات المياه الجوفية وضع سابقة واضحة: الزراعة المكثفة للمياه في الحقول المفتوحة غير قابلة للاستمرار. هذا يجعل الزراعة في البيئات المحكومة (CEA) — ليس خياراً، بل <strong>ضرورة استراتيجية</strong> لأي مبادرة زراعية جديدة في المملكة."},
    "insight_label": {"en": "Key Insight:", "zh": "关键洞察：", "ar": "رؤية رئيسية:"},
    "insight_text": {"en": "PIF has already placed its bets — Saudi Coffee Company (2022), SALIC ($27B agri portfolio), Topian (NEOM food systems), Green Dunes (vertical farming). What's missing is the <em>core technology platform</em> that can make coffee cultivation viable in Saudi Arabia's climate. Napell's patented gas-liquid atomization system + AI robotic tissue culture is precisely that missing piece — and it is ready for deployment.", "zh": "PIF已经布局——Saudi Coffee Company（2022年）、SALIC（270亿美元农业组合）、Topian（NEOM食品系统）、Green Dunes（垂直农业）。缺少的是能让咖啡种植在沙特气候下可行的<em>核心技术平台</em>。Napell的专利气液式雾化系统+AI机器人组培正是这一缺失的拼图——且已准备好部署。", "ar": "صندوق الاستثمارات العامة رهن بالفعل — شركة القهوة السعودية (2022)، ساليك (محفظة زراعية 27 مليار دولار)، توبيان (أنظمة غذاء نيوم)، الكثبان الخضراء (الزراعة العمودية). ما ينقص هو <em>منصة التقنية الأساسية</em> التي يمكن أن تجعل زراعة القهوة ممكنة في مناخ السعودية. نظام الضبوب بالغاز والسائل المسجل لـ Napell + زراعة الأنسجة بالروبوت هو بالضبط تلك القطعة المفقودة — وهو جاهز للنشر."},
  },

  "technology": {
    "sec_num": {"en": "Section 03", "zh": "第 03 节", "ar": "القسم 03"},
    "sec_title": {"en": "Proprietary Technology Platform", "zh": "专利技术平台", "ar": "منصة التقنية المسجلة"},
    "sec_desc": {"en": "The patented system that makes desert coffee cultivation viable.", "zh": "使沙漠咖啡种植成为可能的专利系统。", "ar": "النظام المسجل الذي يجعل زراعة القهوة الصحراوية ممكنة."},
    "patent_title": {"en": "Patented Technology", "zh": "专利技术", "ar": "تقنية مسجلة"},
    "patent_info": {"en": "Application No: <strong>202611094298.6</strong> | Filed: July 22, 2026 | China National Intellectual Property Administration", "zh": "申请号：<strong>202611094298.6</strong> | 申请日：2026年7月22日 | 中国国家知识产权局", "ar": "رقم الطلب: <strong>202611094298.6</strong> | تاريخ التقديم: 22 يوليو 2026 | الإدارة الوطنية الصينية للملكية الفكرية"},
    "patent_name": {"en": "Title: <strong>\"Method and System for Full-Cycle Planting Management Based on Gas-Liquid Atomization\"</strong>", "zh": "名称：<strong>\"基于气液式雾化的全周期种植管理方法及系统\"</strong>", "ar": "العنوان: <strong>\"طريقة ونظام إدارة الزراعة طوال الدورة بناءً على الضبوب بالغاز والسائل\"</strong>"},
    "patent_applicant": {"en": "", "zh": "", "ar": ""},
    "patent_claims": {"en": "10 Claims | 15-page Specification | 3-page Drawings", "zh": "10项权利要求 | 15页说明书 | 3页附图", "ar": "10 مطالبات | مواصفات 15 صفحة | رسومات 3 صفحات"},
    "s1_title": {"en": "System 1 — AI Robotic Tissue Culture", "zh": "系统一 — AI机器人组培", "ar": "النظام 1 — زراعة الأنسجة بالروبوت الذكي"},
    "s1_desc": {"en": "An A3-class six-axis collaborative robot (repeatability ±0.02mm) driven by end-to-end deep learning models trained on 2,100+ expert demonstrations and 100K+ simulation epochs performs:", "zh": "A3级六轴协作机器人（重复精度±0.02mm），由端到端深度学习模型驱动，基于2,100+专家演示和10万+模拟轮次训练，可执行：", "ar": "روبوت تعاوني ذو محاور ستة من فئة A3 (دقة تكرار ±0.02 مم) مدعوم بنماذج تعلم عميق شاملة مدربة على أكثر من 2,100 عرض توضيحي للخبراء و100,000+ جولة محاكاة ينفذ:"},
    "s1_li1": {"en": "Stem-tip isolation &amp; callus micro-cutting (0.3N constant force)", "zh": "茎尖分离与愈伤组织微切割（0.3N恒力）", "ar": "عزل قمة الساق والقطع الدقيق للكالس (قوة ثابتة 0.3 نيوتن)"},
    "s1_li2": {"en": "\"Swing operation\" — 8-pattern swirling at 2Hz, 15mm amplitude for somatic embryo suspension", "zh": "\"摇操作\" — 2Hz频率、15mm振幅的8字型摇动，用于体细胞胚悬浮", "ar": "\"عملية التأرجح\" — دوامة بنمط 8 عند 2 هرتز، سعة 15 مم لتعليق الأجنة الجسدية"},
    "s1_li3": {"en": "Real-time 3D vision (60fps structured light, 150ms re-planning latency)", "zh": "实时3D视觉（60fps结构光，150ms重规划延迟）", "ar": "رؤية ثلاثية الأبعاد في الوقت الفعلي (ضوء مهيكل 60 إطار/ثانية، تأخير إعادة التخطيط 150 مللي ثانية)"},
    "s1_li4": {"en": "Dynamic position tracking — adapts to moved/rotated containers mid-operation", "zh": "动态位置追踪 — 操作中可适应移动/旋转的容器", "ar": "تتبع الموضع الديناميكي — يتكيف مع الحاويات المتحركة/المستدارة أثناء العملية"},
    "s1_li5": {"en": "Full subculture cycle: \"cut-transfer-inoculate\" in 22 sec/seedling (1.5× human speed, 24/7)", "zh": "完整继代周期：\"切-移-接\" 22秒/株（1.5倍人工速度，24/7）", "ar": "دورة الزراعة الفرعية الكاملة: \"قطع-نقل-تطعيم\" في 22 ثانية/شتلة (1.5× سرعة الإنسان، 24/7)"},
    "s1_li6": {"en": "1 mother plant → 1,000,000+ clones/year with 92%+ somatic embryogenesis sync rate", "zh": "1株母株 → 100万+克隆/年，体细胞胚同步化率92%+", "ar": "نبتة أم واحدة → أكثر من 1,000,000 نسخة/سنة بمعدل تزامن تكوين الأجنة الجسدية 92%+"},
    "s1_li7": {"en": "Contamination rate &lt; 0.2% in closed automated system", "zh": "封闭自动化系统污染率 &lt; 0.2%", "ar": "معدل التلوث &lt; 0.2% في النظام الآلي المغلق"},
    "s2_title": {"en": "System 2 — Gas-Liquid Atomization Hydroponics", "zh": "系统二 — 气液式雾化水培", "ar": "النظام 2 — الزراعة المائية الضبابية بالغاز والسائل"},
    "s2_desc": {"en": "Ultrasonic 1.7MHz atomizers generate 5-30μm nutrient mist droplets — 300% more root oxygenation than deep-water hydroponics. Combined with the full-cycle management system:", "zh": "超声波1.7MHz雾化器产生5-30μm营养雾滴——根系供氧量比深液流水培高300%。结合全周期管理系统：", "ar": "مرذاذات فوق صوتية بتردد 1.7 ميجاهرتز تنتج قطرات ضباب مغذية 5-30 ميكرومتر — أكسجين جذور أعلى بنسبة 300% من الزراعة المائية العميقة. مدمج مع نظام إدارة الدورة الكاملة:"},
    "s2_li1": {"en": "Zero-buffer transplant: robotic root washing → sponge collar → atomization tube insertion (99.5% survival)", "zh": "零缓冲移栽：机器人洗根 → 海绵卡环 → 雾化管插入（99.5%成活率）", "ar": "زرع بدون مخزن مؤقت: غسيل جذر آلي → طوقاً إسفنجياً → إدخال أنبوب الضبوب (99.5% بقاء)"},
    "s2_li2": {"en": "Gradient seedling hardening: 3-day auto ramp (95%→70% RH, 1000→5000 lux)", "zh": "梯度炼苗：3天自动调节（95%→70%湿度，1000→5000勒克斯）", "ar": "تقسية الشتلات المتدرجة: منحدر تلقائي 3 أيام (95%→70% رطوبة، 1000→5000 لوكس)"},
    "s2_li3": {"en": "Custom nutrient formulas per variety: N:210, P:31, K:235, Ca:180, Mg:48 mg/L (Typica)", "zh": "按品种定制营养液配方：N:210, P:31, K:235, Ca:180, Mg:48 mg/L（铁皮卡）", "ar": "تركيبات مغذية مخصصة لكل صنف: N:210, P:31, K:235, Ca:180, Mg:48 ملغم/لتر (تيبيكا)"},
    "s2_li4": {"en": "Flowering induction: P/K boost + short-day + 16-18°C nights → first bloom at 12-14 months", "zh": "开花诱导：磷钾提升+短日照+16-18°C夜间 → 12-14个月首次开花", "ar": "تحفيز الإزهار: تعزيز P/K + يوم قصير + ليالي 16-18°م → أول تفتح في 14-12 شهر"},
    "s2_li5": {"en": "15 sec spray / 3 min pause cycle, midnight rest period", "zh": "喷雾15秒/暂停3分钟循环，午夜休息", "ar": "دورة 15 ثانية رش / 3 دقائق توقف، فترة راحة منتصف الليل"},
    "s2_li6": {"en": "Closed-loop water circuit: 90% recovery, zero discharge", "zh": "闭环水循环：90%回收，零排放", "ar": "دائرة مياه مغلقة: 90% استرجاع، صفر تصريف"},
    "s2_li7": {"en": "Water consumption: 2,100 L/kg cherry vs. 21,000 L for traditional farming", "zh": "用水量：2,100升/公斤咖啡鲜果 vs 传统种植21,000升", "ar": "استهلاك المياه: 2,100 لتر/كجم كرز مقابل 21,000 لتر للزراعة التقليدية"},
    "metric1_val": {"en": "15×", "zh": "15×", "ar": "15×"},
    "metric1_lbl": {"en": "Yield vs. Traditional Farm", "zh": "产量 vs 传统农场", "ar": "الإنتاج مقابل المزرعة التقليدية"},
    "metric1_desc": {"en": "5-8 kg cherry/m²/year vs. 0.4 kg in open field", "zh": "5-8公斤鲜果/m²/年 vs 露天0.4公斤", "ar": "5-8 كجم كرز/م²/سنة مقابل 0.4 كجم في الحقل المفتوح"},
    "metric2_val": {"en": "12-14 mo", "zh": "12-14个月", "ar": "14-12 شهر"},
    "metric2_lbl": {"en": "First Harvest", "zh": "首次收获", "ar": "أول حصاد"},
    "metric2_desc": {"en": "vs. 3-4 years in traditional plantation", "zh": "vs 传统种植3-4年", "ar": "مقابل 3-4 سنوات في المزرعة التقليدية"},
    "metric3_val": {"en": "90%", "zh": "90%", "ar": "90%"},
    "metric3_lbl": {"en": "Water Reduction", "zh": "节水率", "ar": "تقليل المياه"},
    "metric3_desc": {"en": "vs. traditional open-field irrigation", "zh": "vs 传统露天灌溉", "ar": "مقابل الري التقليدي في الحقول المفتوحة"},
  },

  "market": {
    "sec_num": {"en": "Section 04", "zh": "第 04 节", "ar": "القسم 04"},
    "sec_title": {"en": "Market Opportunity & Data", "zh": "市场机遇与数据", "ar": "فرصة السوق والبيانات"},
    "sec_desc": {"en": "Saudi coffee market metrics and the import substitution opportunity.", "zh": "沙特咖啡市场指标与进口替代机遇。", "ar": "مؤشرات سوق القهوة السعودي وفرصة استبدال الاستيراد."},
    "t1_title": {"en": "Saudi Coffee Market Size & Growth", "zh": "沙特咖啡市场规模与增长", "ar": "حجم ونمو سوق القهوة السعودي"},
    "t1_chart_title": {"en": "Saudi Arabia Coffee Market: Import Volume & Value Growth", "zh": "沙特阿拉伯咖啡市场：进口量与价值增长", "ar": "سوق القهوة في السعودية: نمو حجم وقيمة الاستيراد"},
    "t2_title": {"en": "Import Substitution Opportunity", "zh": "进口替代机遇", "ar": "فرصة استبدال الاستيراد"},
    "t2_chart_title": {"en": "Projected Import Substitution: Napell × PIF Scenario", "zh": "进口替代预测：Napell × PIF情景", "ar": "استبدال الاستيراد المتوقع: سيناريو Napell × PIF"},
    "t2_note": {"en": "Saudi import data shows a structural trend: volumes grew 20% YoY, while value surged 52% due to price inflation. Brazil's drought crisis and China's 150% consumption growth are creating sustained upward price pressure. A sovereign domestic supply is a <strong>macroeconomic hedge</strong>, not just a commercial play.", "zh": "沙特进口数据显示结构性趋势：量同比增长20%，而价值因价格通胀激增52%。巴西干旱危机和中国150%的消费增长正在制造持续的上涨价格压力。主权国内供应不仅是商业行为，更是<strong>宏观经济对冲</strong>。", "ar": "تظهر بيانات الاستيراد السعودية اتجاهاً هيكلياً: نمت الأحجام 20% سنوياً، بينما ارتفعت القيمة 52% بسبب تضخم الأسعار. أزمة الجفاف في البرازيل ونمو الاستهلاك الصيني 150% يخلقان ضغط أسعار تصاعدي مستمر. الإمداد المحلي السيادي هو <strong>تحوط اقتصادي كلي</strong>، ليس مجرد صفقة تجارية."},
  },

  "proposal": {
    "sec_num": {"en": "Section 05", "zh": "第 05 节", "ar": "القسم 05"},
    "sec_title": {"en": "The Partnership Proposal", "zh": "合作提案", "ar": "عرض الشراكة"},
    "sec_desc": {"en": "A joint venture structure for sovereign coffee capability.", "zh": "建立主权咖啡能力的合资企业结构。", "ar": "هيكل مشروع مشترك لقدرة القهوة السيادية."},
    "pif_title": {"en": "PIF Contribution", "zh": "PIF贡献", "ar": "مساهمة صندوق الاستثمارات"},
    "pif_li1": {"en": "<strong>$200-250M staged investment</strong> over 7 years (Phases 1-3)", "zh": "<strong>2-2.5亿美元分期投资</strong>，7年内（阶段1-3）", "ar": "<strong>استثمار مرحلي 200-250 مليون دولار</strong> على مدى 7 سنوات (المراحل 1-3)"},
    "pif_li2": {"en": "Land allocation &amp; regulatory facilitation (NEOM, Jazan, or Al-Baha)", "zh": "土地分配与监管便利（NEOM、吉赞或巴哈）", "ar": "تخصيص الأرض وتسهيلات تنظيمية (نيوم، جازان، أو الباحة)"},
    "pif_li3": {"en": "Corporate vehicle formation under Saudi law", "zh": "依沙特法律组建企业实体", "ar": "تأسيس كيان مؤسسي بموجب القانون السعودي"},
    "pif_li4": {"en": "Access to PIF portfolio synergy: Saudi Coffee Company, SALIC, Topian", "zh": "接入PIF投资组合协同：Saudi Coffee Company、SALIC、Topian", "ar": "الوصول إلى تأثير محفظة PIF: شركة القهوة السعودية، ساليك، توبيان"},
    "pif_li5": {"en": "Saudi talent pipeline via MEWA / KACST / KAUST partnerships", "zh": "通过MEWA/KACST/KAUST合作建立沙特人才管道", "ar": "خط أنابيب المواهب السعودية عبر شراكات MEWA / KACST / KAUST"},
    "pif_li6": {"en": "Market access: government procurement, Hajj/Umrah catering, GCC export", "zh": "市场准入：政府采购、朝觐/副朝餐饮、海合会出口", "ar": "الوصول إلى السوق: المشتريات الحكومية، تموين الحج/العمرة، تصدير مجلس التعاون الخليجي"},
    "pif_li7": {"en": "Brand co-ownership: \"Saudi Origin\" label with PIF sovereign backing", "zh": "品牌共有：\"沙特原产地\"标签，PIF主权背书", "ar": "الملكية المشتركة للعلامة: علامة \"المنشأ السعودي\" مع ضمان PIF السيادي"},
    "napell_title": {"en": "Napell Contribution", "zh": "Napell贡献", "ar": "مساهمة Napell"},
    "napell_li1": {"en": "<strong>Patent license (CN 202611094298.6)</strong> — exclusive MENA rights", "zh": "<strong>专利授权（CN 202611094298.6）</strong> — MENA地区独占权", "ar": "<strong>ترخيص براءة الاختراع (CN 202611094298.6)</strong> — حقوق حصرية لمنطقة MENA"},
    "napell_li2": {"en": "Complete technology transfer: AI robot tissue culture + atomization hydroponics", "zh": "完整技术转移：AI机器人组培+雾化水培", "ar": "نقل تقني كامل: زراعة الأنسجة بالروبوت الذكي + الزراعة المائية الضبابية"},
    "napell_li3": {"en": "A3 robotic hardware specification &amp; integration know-how", "zh": "A3机器人硬件规格与集成专有技术", "ar": "مواصفات أجهزة الروبوت A3 ومعرفة التكامل"},
    "napell_li4": {"en": "AI vision model training pipeline (2,100+ expert demonstrations)", "zh": "AI视觉模型训练流水线（2,100+专家演示）", "ar": "خط أنابيب تدريب نموذج الرؤية الذكي (2,100+ عرض توضيحي للخبراء)"},
    "napell_li5": {"en": "Custom nutrient formula IP for Arabica &amp; Robusta (50+ variety library)", "zh": "阿拉比卡和罗布斯塔定制营养液配方IP（50+品种库）", "ar": "ملكية فكرية لتركيبات المغذيات المخصصة لأرابيكا وروبوستا (مكتبة 50+ صنف)"},
    "napell_li6": {"en": "Facility design &amp; engineering blueprints (50,000 m² template)", "zh": "设施设计与工程蓝图（50,000 m²模板）", "ar": "تصميم المنشأة والمخططات الهندسية (قالب 50,000 م²)"},
    "napell_li7": {"en": "On-site deployment team (20+ engineers for Phase 1, 18-24 months)", "zh": "现场部署团队（阶段一20+工程师，18-24个月）", "ar": "فريق النشر الميداني (20+ مهندس للمرحلة 1، 18-24 شهراً)"},
    "napell_li8": {"en": "Saudi team training &amp; certification program", "zh": "沙特团队培训与认证项目", "ar": "برنامج تدريب واعتماد الفريق السعودي"},
    "napell_li9": {"en": "Continuous R&amp;D: new varieties, efficiency optimization, digital twin", "zh": "持续研发：新品种、效率优化、数字孪生", "ar": "بحث وتطوير مستمر: أصناف جديدة، تحسين الكفاءة، التوأم الرقمي"},
    "jv_title": {"en": "Proposed JV Structure", "zh": "拟议合资结构", "ar": "هيكل المشروع المشترك المقترح"},
    "jv_pif_lbl": {"en": "PIF / Saudi Entity", "zh": "PIF / 沙特实体", "ar": "PIF / الكيان السعودي"},
    "jv_napell_lbl": {"en": "Napell Biotech", "zh": "Napell Biotech", "ar": "Napell Biotech"},
    "jv_entity": {"en": "Saudi Coffee Technology Co.", "zh": "沙特咖啡科技有限公司", "ar": "شركة تقنية القهوة السعودية"},
    "jv_entity_note": {"en": "(proposed entity name)", "zh": "（拟议实体名称）", "ar": "(اسم الكيان المقترح)"},
  },

  "roadmap": {
    "sec_num": {"en": "Section 06", "zh": "第 06 节", "ar": "القسم 06"},
    "sec_title": {"en": "Implementation Roadmap", "zh": "实施路线图", "ar": "خارطة طريق التنفيذ"},
    "sec_desc": {"en": "Seven-year phased deployment with clear milestones.", "zh": "七年分阶段部署与明确里程碑。", "ar": "نشر مرحلي لمدة سبع سنوات مع معالم واضحة."},
    "p1_label": {"en": "Phase 1 — Year 1-2", "zh": "阶段一 — 第1-2年", "ar": "المرحلة 1 — السنة 1-2"},
    "p1_title": {"en": "R&amp;D Center + Pilot Farm ($25-35M)", "zh": "研发中心+试验农场（2,500-3,500万美元）", "ar": "مركز البحث والتطوير + مزرعة تجريبية (25-35 مليون دولار)"},
    "p1_li1": {"en": "Establish JV legal entity under Saudi law", "zh": "依沙特法律成立合资法律实体", "ar": "تأسيس كيان قانوني مشترك بموجب القانون السعودي"},
    "p1_li2": {"en": "Deploy 2 A3 robotic tissue culture lines + AI vision system", "zh": "部署2条A3机器人组培产线+AI视觉系统", "ar": "نشر خطين لزراعة الأنسجة بالروبوت A3 + نظام الرؤية الذكي"},
    "p1_li3": {"en": "Build 500 m² pilot atomization hydroponic farm", "zh": "建设500 m²试验雾化水培农场", "ar": "بناء مزرعة ضبابية مائية تجريبية 500 م²"},
    "p1_li4": {"en": "Saudi coffee variety adaptation trials (Typica, Bourbon, Geisha, local Khulani)", "zh": "沙特咖啡品种适应性试验（铁皮卡、波旁、瑰夏、本地胡拉尼）", "ar": "تجارب تكييف أصناف القهوة السعودية (تيبيكا، بوربون، جيشا، الخولاني المحلي)"},
    "p1_li5": {"en": "Train first cohort of 20 Saudi agri-tech engineers", "zh": "培训首批20名沙特农业科技工程师", "ar": "تدريب الدفعة الأولى من 20 مهندس زراعي سعودي"},
    "p1_li6": {"en": "Site selection &amp; permitting: NEOM / Jazan / Al-Baha", "zh": "选址与许可：NEOM/吉赞/巴哈", "ar": "اختيار الموقع والترخيص: نيوم / جازان / الباحة"},
    "p1_li7": {"en": "Milestone: First Saudi-grown cup of coffee served (Month 18)", "zh": "里程碑：第18个月供应首杯沙特种植咖啡", "ar": "معلم: تقديم أول فنجان قهوة مزروع في السعودية (الشهر 18)"},
    "p2_label": {"en": "Phase 2 — Year 2-4", "zh": "阶段二 — 第2-4年", "ar": "المرحلة 2 — السنة 2-4"},
    "p2_title": {"en": "Commercial-Scale Vertical Farm ($80-120M)", "zh": "商业规模垂直农场（8,000-12,000万美元）", "ar": "مزرعة عمودية تجارية (80-120 مليون دولار)"},
    "p2_li1": {"en": "Construct 50,000 m² controlled-environment facility", "zh": "建设50,000 m²受控环境设施", "ar": "بناء منشأة بيئة محكومة 50,000 م²"},
    "p2_li2": {"en": "12,000 m² atomization hall (4-level vertical racking = 48,000 m² grow area)", "zh": "12,000 m²雾化大厅（4层垂直架=48,000 m²种植面积）", "ar": "قاعة ضبوب 12,000 م² (رفوف عمودية 4 مستويات = 48,000 م² مساحة زراعة)"},
    "p2_li3": {"en": "Install processing, roasting &amp; packaging line (Zone 3)", "zh": "安装加工、烘焙和包装线（3区）", "ar": "تركيب خط المعالجة والتحميص والتعبئة (المنطقة 3)"},
    "p2_li4": {"en": "Deploy 4MWp solar PV + 8MWh battery storage + RO water system", "zh": "部署4MWp太阳能光伏+8MWh电池储能+RO水系统", "ar": "نشر 4MWp طاقة شمسية + تخزين بطاريات 8MWh + نظام مياه RO"},
    "p2_li5": {"en": "Expand team to 150+ local technicians &amp; engineers", "zh": "团队扩展至150+本地技术人员和工程师", "ar": "توسيع الفريق إلى 150+ فني ومهندس محلي"},
    "p2_li6": {"en": "Launch \"Saudi Origin\" specialty coffee brand", "zh": "推出\"沙特原产地\"精品咖啡品牌", "ar": "إطلاق علامة قهوة مختصة \"المنشأ السعودي\""},
    "p2_li7": {"en": "Initial B2B supply to Saudi cafes (60,000+ establishments)", "zh": "初步B2B供应沙特咖啡馆（60,000+门店）", "ar": "إمداد أولي B2B لمقاهي السعودية (60,000+ منشأة)"},
    "p2_li8": {"en": "Output: 240-384 tons cherry / year → 48-77 tons green bean", "zh": "产量：240-384吨鲜果/年 → 48-77吨生豆", "ar": "الإنتاج: 240-384 طن كرز / سنة → 48-77 طن حبوب خضراء"},
    "p3_label": {"en": "Phase 3 — Year 5-7", "zh": "阶段三 — 第5-7年", "ar": "المرحلة 3 — السنة 5-7"},
    "p3_title": {"en": "National Scale &amp; GCC Export ($150-250M cumulative)", "zh": "全国规模与海合会出口（累计1.5-2.5亿美元）", "ar": "نطاق وطني وتصدير خليجي (150-250 مليون دولار تراكمي)"},
    "p3_li1": {"en": "Expand to 3 facilities across Saudi Arabia", "zh": "扩展至沙特全国3个设施", "ar": "التوسع إلى 3 منشآت في جميع أنحاء السعودية"},
    "p3_li2": {"en": "10M+ plantlets/year tissue culture capacity", "zh": "组培产能1,000万+株/年", "ar": "سعة زراعة الأنسجة 10M+ شتلة/سنة"},
    "p3_li3": {"en": "GCC export hub: UAE, Kuwait, Qatar, Bahrain markets", "zh": "海合会出口枢纽：阿联酋、科威特、卡塔尔、巴林市场", "ar": "مركز تصدير خليجي: أسواق الإمارات، الكويت، قطر، البحرين"},
    "p3_li4": {"en": "Achieve specialty-grade cupping scores 85+", "zh": "达到精品级杯测评分85+", "ar": "تحقيق درجات تذوق متخصصة 85+"},
    "p3_li5": {"en": "Open Saudi Coffee Tourism &amp; Experience Center", "zh": "开设沙特咖啡旅游与体验中心", "ar": "افتتاح مركز السياحة والتجربة القهوة السعودية"},
    "p3_li6": {"en": "IP licensing model for additional GCC nations", "zh": "面向其他海合会国家的IP授权模式", "ar": "نموذج ترخيص الملكية الفكرية لدول الخليج الإضافية"},
    "p3_li7": {"en": "Target: 5-8% Saudi import substitution (14,000+ tons/year)", "zh": "目标：5-8%沙特进口替代（14,000+吨/年）", "ar": "الهدف: 5-8% استبدال استيراد السعودية (14,000+ طن/سنة)"},
    "p3_li8": {"en": "Total team: 350+ high-skilled positions", "zh": "总团队：350+高技能岗位", "ar": "إجمالي الفريق: 350+ وظيفة عالية المهارة"},
    "p4_label": {"en": "Phase 4 — Year 8-10", "zh": "阶段四 — 第8-10年", "ar": "المرحلة 4 — السنة 8-10"},
    "p4_title": {"en": "Global Brand &amp; Digital Twin Era", "zh": "全球品牌与数字孪生时代", "ar": "علامة عالمية وعصر التوأم الرقمي"},
    "p4_li1": {"en": "Deploy \"light-machine-plant\" integrated digital twin system", "zh": "部署\"光-机-植\"一体化数字孪生系统", "ar": "نشر نظام التوأم الرقمي المتكامل \"ضوء-آلة-نبات\""},
    "p4_li2": {"en": "AI-predictive harvest optimization per plant", "zh": "AI预测每株收获优化", "ar": "تحسين الحصاد التنبؤي بالذكاء الاصطناعي لكل نبتة"},
    "p4_li3": {"en": "Blockchain full traceability: \"from somatic cell to cup\"", "zh": "区块链全溯源：\"从体细胞到杯子\"", "ar": "تتبع كامل بالبلوكتشين: \"من الخلية الجسدية إلى الفنجان\""},
    "p4_li4": {"en": "Target: 15% import substitution (36,000+ tons/year)", "zh": "目标：15%进口替代（36,000+吨/年）", "ar": "الهدف: 15% استبدال الاستيراد (36,000+ طن/سنة)"},
    "p4_li5": {"en": "\"Saudi Origin\" as globally recognized specialty coffee brand", "zh": "\"沙特原产地\"成为全球认可的精品咖啡品牌", "ar": "\"المنشأ السعودي\" كعلامة قهوة مختصة معترف بها عالمياً"},
    "p4_li6": {"en": "Technology export to other arid-region nations (MENA, Australia, S. Africa)", "zh": "技术出口至其他干旱地区国家（中东非、澳大利亚、南非）", "ar": "تصدير التقنية إلى دول المناطق القاحلة الأخرى (MENA، أستراليا، جنوب أفريقيا)"},
  },

  "financials": {
    "sec_num": {"en": "Section 07", "zh": "第 07 节", "ar": "القسم 07"},
    "sec_title": {"en": "Financial Projections", "zh": "财务预测", "ar": "التوقعات المالية"},
    "sec_desc": {"en": "Unit economics, revenue streams, and return profile.", "zh": "单位经济效益、收入来源和回报概况。", "ar": "اقتصاديات الوحدة ومصادر الإيرادات وملف العائد."},
    "t1_title": {"en": "Investment Allocation", "zh": "投资分配", "ar": "توزيع الاستثمار"},
    "t2_title": {"en": "Projected P&L Summary (Year 5)", "zh": "预测损益摘要（第5年）", "ar": "ملخص الأرباح والخسائر المتوقع (السنة 5)"},
    "chart_title": {"en": "10-Year Revenue & EBITDA Projection", "zh": "10年收入与EBITDA预测", "ar": "توقعات الإيرادات وEBITDA لـ 10 سنوات"},
    "m1_val": {"en": "5-7 yr", "zh": "5-7年", "ar": "5-7 سنة"},
    "m1_lbl": {"en": "Payback Period", "zh": "回本期", "ar": "فترة الاسترداد"},
    "m2_val": {"en": "18-24%", "zh": "18-24%", "ar": "18-24%"},
    "m2_lbl": {"en": "Project IRR", "zh": "项目IRR", "ar": "IRR المشروع"},
    "m3_val": {"en": "3.5-4.5×", "zh": "3.5-4.5×", "ar": "3.5-4.5×"},
    "m3_lbl": {"en": "MOIC (10-year)", "zh": "MOIC（10年）", "ar": "MOIC (10 سنوات)"},
    "m4_val": {"en": "350+", "zh": "350+", "ar": "+350"},
    "m4_lbl": {"en": "Jobs Created (high-skilled)", "zh": "创造就业（高技能）", "ar": "وظائف_created (عالية المهارة)"},
  },

  "risks": {
    "sec_num": {"en": "Section 08", "zh": "第 08 节", "ar": "القسم 08"},
    "sec_title": {"en": "Risk Analysis & Mitigation", "zh": "风险分析与缓解", "ar": "تحليل المخاطر والتخفيف"},
    "sec_desc": {"en": "Key risks identified with mitigation strategies.", "zh": "已识别关键风险及缓解策略。", "ar": "المخاطر الرئيسية المحددة مع استراتيجيات التخفيف."},
    "r1_name": {"en": "Energy Cost", "zh": "能源成本", "ar": "تكلفة الطاقة"},
    "r1_sev": {"en": "Medium", "zh": "中", "ar": "متوسط"},
    "r1_desc": {"en": "Indoor CEA requires significant electricity for LED lighting and climate control.", "zh": "室内CEA需要大量电力用于LED照明和气候控制。", "ar": "تتطلب الزراعة المحكومة الداخلية كهرباء كبيرة للإضاءة LED والتحكم في المناخ."},
    "r1_mit": {"en": "Saudi Arabia has world-class solar resource (GHI 2,200+ kWh/m²/yr). Facility design includes 4MWp on-site solar + 8MWh battery targeting 95%+ energy self-sufficiency. Saudi electricity tariffs are among the lowest globally.", "zh": "沙特拥有世界级太阳能资源（GHI 2,200+ kWh/m²/年）。设施设计包括4MWp现场太阳能+8MWh电池，目标95%+能源自给。沙特电价全球最低之一。", "ar": "تمتلك السعودية موارد شمسية عالمية المستوى (GHI 2,200+ kWh/m²/سنة). يشمل تصميم المنشأة طاقة شمسية 4MWp + بطاريات 8MWh باستهداف 95%+ اكتفاء ذاتي. تعرفة الكهرباء السعودية من الأدنى عالمياً."},
    "r2_name": {"en": "Technology Transfer", "zh": "技术转移", "ar": "نقل التقنية"},
    "r2_sev": {"en": "Medium", "zh": "中", "ar": "متوسط"},
    "r2_desc": {"en": "Complex AI-robotic system requires skilled operators.", "zh": "复杂的AI机器人系统需要熟练操作员。", "ar": "نظام الروبوت الذكي المعقد يتطلب مشغلين مهرة."},
    "r2_mit": {"en": "Structured 18-24 month training program for Saudi engineers. KAUST/KACST partnership for ongoing talent pipeline. Remote diagnostics + on-site support team.", "zh": "为沙特工程师提供18-24个月结构化培训项目。KAUST/KACST合作持续人才管道。远程诊断+现场支持团队。", "ar": "برنامج تدريب منظم 18-24 شهراً للمهندسين السعوديين. شراكة KAUST/KACST لخط أنابيب المواهب المستمر. تشخيص عن بعد + فريق دعم ميداني."},
    "r3_name": {"en": "Long-term Reliability", "zh": "长期可靠性", "ar": "الموثوقية طويلة الأمد"},
    "r3_sev": {"en": "Medium", "zh": "中", "ar": "متوسط"},
    "r3_desc": {"en": "Robot arm degradation in high-humidity, weakly acidic mist environment.", "zh": "机械臂在高湿、弱酸雾化环境中的退化。", "ar": "تدهور الذراع الروبوتي في بيئة رطبة عالية وضباب حمضي ضعيف."},
    "r3_mit": {"en": "Phase 1 pilot validates durability under real conditions. IP65-rated arm variants. Predictive maintenance via IoT sensor suite. Annual molecular marker check for somaclonal variation.", "zh": "阶段一试验验证真实条件下耐久性。IP65等级机械臂变体。通过IoT传感器套件进行预测性维护。年度分子标记检查体细胞无性系变异。", "ar": "المرحلة 1 التجريبية تتحقق من المتانة في ظروف حقيقية. متغيرات ذراع بمستوى IP65. صيانة تنبؤية عبر مجموعة حساسات IoT. فحص جزيئي سنوي للتغيرات الجسدية."},
    "r4_name": {"en": "Market Acceptance", "zh": "市场接受度", "ar": "قبول السوق"},
    "r4_sev": {"en": "Low", "zh": "低", "ar": "منخفض"},
    "r4_desc": {"en": "\"Lab-grown\" coffee may face consumer perception barriers.", "zh": "\"实验室种植\"咖啡可能面临消费者认知障碍。", "ar": "القهوة \"المزروعة في المختبر\" قد تواجه حواجز تصور المستهلك."},
    "r4_mit": {"en": "\"Saudi Origin\" brand positioning emphasizes heritage + innovation. Transparency via blockchain traceability. Saudi Coffee Company brand integration provides instant credibility. PIF sovereign backing = quality assurance.", "zh": "\"沙特原产地\"品牌定位强调传承+创新。通过区块链溯源实现透明度。Saudi Coffee Company品牌整合提供即时信誉。PIF主权背书=质量保证。", "ar": "تمركز علامة \"المنشأ السعودي\" يبرز التراث + الابتكار. الشفافية عبر التتبع بالبلوكتشين. تكامل علامة شركة القهوة السعودية يوفر مصداقية فورية. ضمان PIF السيادي = ضمان الجودة."},
    "r5_name": {"en": "Regulatory", "zh": "监管", "ar": "تنظيمي"},
    "r5_sev": {"en": "Low", "zh": "低", "ar": "منخفض"},
    "r5_desc": {"en": "Organic certification for hydroponic coffee; import regulations.", "zh": "水培咖啡有机认证；进口法规。", "ar": "شهادة عضوية للقهوة المائية؛ لوائح الاستيراد."},
    "r5_mit": {"en": "Align with SFDA / MEWA early. \"Controlled Environment Grown\" certification pathway. Saudi government is proactively enabling agritech regulation as part of Vision 2030.", "zh": "早期与SFDA/MEWA对接。\"受控环境种植\"认证路径。沙特政府正积极推动农业科技监管作为愿景2030的一部分。", "ar": "التوافق المبكر مع SFDA / MEWA. مسار شهادة \"مزروع في بيئة محكومة\". الحكومة السعودية تمكن استباقياً تنظيم التقنية الزراعية كجزء من رؤية 2030."},
    "r6_name": {"en": "Water Supply", "zh": "供水", "ar": "إمداد المياه"},
    "r6_sev": {"en": "Low", "zh": "低", "ar": "منخفض"},
    "r6_desc": {"en": "Dependence on desalination water for nutrient solution.", "zh": "依赖海水淡化水配制营养液。", "ar": "الاعتماد على مياه التحلية لمحلول المغذيات."},
    "r6_mit": {"en": "Minimal input water needed (closed-loop 90% recovery). RO desalination unit included in facility design. Unit economics work at Saudi water prices.", "zh": "需最小输入水量（闭环90%回收）。设施设计包含RO淡化装置。单位经济在沙特水价下可行。", "ar": "حد أدنى من مياه المدخلات مطلوب (استرجاع مغلق 90%). وحدة تحلية RO مضمنة في تصميم المنشأة. اقتصاديات الوحدة تعمل بأسعار المياه السعودية."},
  },

  "alignment": {
    "sec_num": {"en": "Section 09", "zh": "第 09 节", "ar": "القسم 09"},
    "sec_title": {"en": "Strategic Alignment: PIF & Vision 2030", "zh": "战略对齐：PIF与愿景2030", "ar": "التوافق الاستراتيجي: PIF ورؤية 2030"},
    "sec_desc": {"en": "How this partnership fits within PIF's existing portfolio and national strategy.", "zh": "此合作如何契合PIF现有投资组合与国家战略。", "ar": "كيف تندرج هذه الشراكة ضمن محفظة PIF الحالية والاستراتيجية الوطنية."},
    "c1_title": {"en": "Food Security", "zh": "粮食安全", "ar": "الأمن الغذائي"},
    "c1_text": {"en": "Directly addresses Saudi Arabia's 80% food import dependency. Creates sovereign capability in a high-value crop with massive domestic demand. Reduces exposure to global coffee price volatility (168% price surge Oct 2023-Feb 2025). Aligns with National Food Security Program (NFSP) targets.", "zh": "直接应对沙特80%的食品进口依赖。在高需求作物中创建主权能力。减少对全球咖啡价格波动的暴露（2023年10月至2025年2月价格上涨168%）。契合国家粮食安全计划（NFSP）目标。", "ar": "يعالج مباشرة اعتماد السعودية بنسبة 80% على استيراد الغذاء. ينشئ قدرة سيادية في محصول عالي القيمة بطلب محلي ضخم. يقلل التعرض لتقلب أسعار القهوة العالمية (ارتفاع الأسعار 168% أكتوبر 2023-فبراير 2025). يتوافق مع أهداف برنامج الأمن الغذائي الوطني (NFSP)."},
    "c2_title": {"en": "Economic Diversification", "zh": "经济多元化", "ar": "التنويع الاقتصادي"},
    "c2_text": {"en": "Builds a new non-oil industry: coffee = SAR 5-7B market domestically, $200B+ globally. Creates 350+ high-skilled technology jobs (not low-wage agricultural labor). Generates export revenue from GCC and global specialty coffee markets. Contributes to PIF's non-oil GDP target.", "zh": "建立新的非石油产业：咖啡=国内市场SAR 50-70亿，全球2,000亿美元+。创造350+高技能技术岗位（非低薪农业劳动力）。从海合会和全球精品咖啡市场产生出口收入。贡献PIF非石油GDP目标。", "ar": "يبني صناعة جديدة غير نفطية: القهوة = سوق محلي 5-7 مليار ريال، 200 مليار دولار+ عالمياً. ينشئ 350+ وظيفة تقنية عالية المهارة (ليس عملاً زراعياً منخفض الأجر). يولد إيرادات تصدير من أسواق الخليج والقهوة المختصة العالمية. يساهم في هدف PIF للناتج المحلي غير النفطي."},
    "c3_title": {"en": "Technology Transfer", "zh": "技术转移", "ar": "نقل التقنية"},
    "c3_text": {"en": "Brings world-first AI-robotic coffee tissue culture to the Kingdom. Patent licensed exclusively for MENA region. Training program develops Saudi expertise in agritech, robotics, AI, plant science. Positions Saudi Arabia as global agritech leader for arid-region agriculture.", "zh": "将世界首创的AI机器人咖啡组培技术引入王国。专利MENA地区独占授权。培训项目培养沙特在农业科技、机器人、AI、植物科学方面的专业能力。使沙特成为干旱地区农业全球科技领导者。", "ar": "يجلب أول زراعة أنسجة قهوة بالروبوت الذكي عالمياً إلى المملكة. براءة اختراع مرخصة حصرياً لمنطقة MENA. برنامج التدريب يطور الخبرة السعودية في التقنية الزراعية والروبوتات والذكاء الاصطناعي وعلوم النبات. يضع السعودية كقائد عالمي في التقنية الزراعية للمناطق القاحلة."},
    "c4_title": {"en": "PIF Portfolio Synergy", "zh": "PIF投资组合协同", "ar": "تأثير محفظة PIF"},
    "c4_text": {"en": "Saudi Coffee Company: technology doubles its production capacity targets. SALIC: Co-investment vehicle for food security mandate. Topian (NEOM): NEOM deployment as global showcase. Green Dunes / NADEC: CEA operational knowledge sharing.", "zh": "Saudi Coffee Company：技术使其产能目标翻倍。SALIC：粮食安全使命的共同投资载体。Topian（NEOM）：NEOM部署作为全球展示。Green Dunes/NADEC：CEA运营知识共享。", "ar": "شركة القهوة السعودية: التقنية تضاعف أهداف طاقتها الإنتاجية. ساليك: مركبة استثمار مشترك لتفويض الأمن الغذائي. توبيان (نيوم): نشر نيوم كعرض عالمي. الكثبان الخضراء / NADEC: مشاركة المعرفة التشغيلية للزراعة المحكومة."},
    "c5_title": {"en": "Tourism & Brand", "zh": "旅游与品牌", "ar": "السياحة والعلامة"},
    "c5_text": {"en": "Coffee tourism center: visitor experience, robot lab tours, coffee museum. \"Saudi Origin\" as premium global coffee brand — analogous to Ethiopian Yirgacheffe or Colombian Supremo. Aligns with 2022 \"Year of Saudi Coffee\" cultural initiative. Hajj/Umrah catering: 20M+ annual visitors — direct market.", "zh": "咖啡旅游中心：访客体验、机器人实验室参观、咖啡博物馆。\"沙特原产地\"作为全球高端咖啡品牌——类比埃塞俄比亚耶加雪菲或哥伦比亚 supremo。契合2022年\"沙特咖啡年\"文化倡议。朝觐/副朝餐饮：2,000万+年度访客——直接市场。", "ar": "مركز السياحة القهوة: تجربة الزوار، جولات مختبر الروبوت، متحف القهوة. \"المنشأ السعودي\" كعلامة قهوة عالمية متميزة — مماثلة ليرغاشيف الإثيوبية أو سوبريمو الكولومبي. يتوافق مع مبادرة \"عام القهوة السعودية\" الثقافية 2022. تموين الحج/العمرة: 20M+ زائر سنوي — سوق مباشر."},
    "c6_title": {"en": "Environmental Leadership", "zh": "环境领导力", "ar": "القيادة البيئية"},
    "c6_text": {"en": "90% water reduction vs traditional farming — critical for water-scarce Saudi Arabia. Closed-loop system: zero wastewater, zero pesticide runoff. Solar-powered, carbon-neutral operation. Urban organic waste → CO₂ enrichment for greenhouse. Positions Saudi Arabia at COP and global climate forums as arid-zone agriculture innovator.", "zh": "比传统种植节水90%——对水资源稀缺的沙特至关重要。闭环系统：零废水、零农药径流。太阳能驱动、碳中和运营。城市有机废物→CO₂温室富集。使沙特在COP和全球气候论坛上成为干旱地区农业创新者。", "ar": "تقليل المياه 90% مقابل الزراعة التقليدية — حرج للسعودية المحدودة المياه. نظام مغلق: صفر مياه عادمة، صرف مبيدات صفر. تشغيل بالطاقة الشمسية، محايد كربونياً. النفايات العضوية الحضرية → إثراء CO₂ للبيوت المحمية. يضع السعودية في COP والمنتديات المناخية العالمية كمبتكر زراعة المناطق القاحلة."},
  },

  "blueprints": {
    "sec_num": {"en": "Section 10", "zh": "第 10 节", "ar": "القسم 10"},
    "sec_title": {"en": "Technical Industrial Blueprints", "zh": "技术工业蓝图", "ar": "المخططات الصناعية الفنية"},
    "sec_desc": {"en": "Detailed engineering drawings for the A3 robotic arm tissue culture system and gas-liquid atomization cultivation principle.", "zh": "A3机械臂组培系统和气液式雾化栽培原理的详细工程图纸。", "ar": "رسومات هندسية تفصيلية لنظام زراعة الأنسجة بالذراع الروبوتي A3 ومبدأ الزراعة الضبابية."},
    "tab1": {"en": "A3 Robotic Arm + AI Vision System", "zh": "A3机械臂 + AI视觉系统", "ar": "ذراع A3 الروبوتي + نظام الرؤية الذكي"},
    "tab2": {"en": "Gas-Liquid Atomization Cultivation", "zh": "气液式雾化栽培系统", "ar": "نظام الزراعة الضبابية بالغاز والسائل"},
    "bp1_title": {"en": "A3 Six-Axis Collaborative Robot + End-to-End AI Vision — Automated Coffee Tissue Culture", "zh": "A3六轴协作机器人 + 端到端AI视觉 — 全自动咖啡组培技术", "ar": "روبوت A3 التعاوني ذو المحاور الستة + رؤية ذكاء اصطناعي شاملة — زراعة أنسجة القهوة الآلية"},
    "bp1_desc": {"en": "This blueprint details the complete A3 robotic arm system: six-axis configuration with ±0.02mm repeatability, 3D structured light vision (0.1mm resolution, 60fps), force-controlled micro-cutting (0.3N, 45° blade angle), the \"swing operation\" for somatic embryo suspension (2Hz, 15mm amplitude), and the end-to-end AI pipeline trained on 2,100+ expert demonstrations and 100,000+ reinforcement learning epochs.", "zh": "本蓝图详细展示了完整的A3机械臂系统：六轴配置（重复精度±0.02mm）、3D结构光视觉（0.1mm分辨率，60fps）、力控微切割（0.3N，45°刀片角度）、体细胞胚悬浮的\"摇操作\"（2Hz，15mm振幅），以及基于2,100+专家演示和100,000+强化学习轮次训练的端到端AI流水线。", "ar": "يفصل هذا المخطط نظام الذراع الروبوتي A3 الكامل: تكوين ستة محاور بدقة تكرار ±0.02 مم، رؤية ضوء ثلاثي الأبعاد مهيكلة (دقة 0.1 مم، 60 إطار/ثانية)، قطع دقيق بالتحكم في القوة (0.3 نيوتن، زاوية شفرة 45°)، \"عملية التأرجح\" لتعليق الأجنة الجسدية (2 هرتز، سعة 15 مم)، وخط أنابيب ذكاء اصطناعي شامل مدرب على أكثر من 2,100 عرض توضيحي للخبراء و100,000+ جولة تعلم تعزيزي."},
    "bp1_caption": {"en": "FIG.1 A3 Six-Axis Robot Operational Config | FIG.2 End-Effector Exploded View | FIG.3 AI Vision Pipeline | FIG.4 Swing Operation Trajectory | FIG.5 Micro-Cutting Sequence | TABLE 1 Key Specifications", "zh": "图1 A3六轴机器人操作配置 | 图2 末端执行器爆炸图 | 图3 AI视觉流水线 | 图4 摇操作轨迹 | 图5 微切割序列 | 表1 关键规格", "ar": "شكل 1 تكوين تشغيل الروبوت A3 ذو المحاور الستة | شكل 2 منظر متفجر للمنفذ النهائي | شكل 3 خط أنابيب الرؤية الذكي | شكل 4 مسار عملية التأرجح | شكل 5 تسلسل القطع الدقيق | جدول 1 المواصفات الرئيسية"},
    "bp1_m1_lbl": {"en": "Repeatability", "zh": "重复精度", "ar": "دقة التكرار"},
    "bp1_m2_lbl": {"en": "Per Seedling Cycle", "zh": "每株周期", "ar": "دورة لكل شتلة"},
    "bp1_m3_lbl": {"en": "RL Training Epochs", "zh": "RL训练轮次", "ar": "دورات تدريب RL"},
    "bp2_title": {"en": "Gas-Liquid Atomization Cultivation System — Aeroponic Coffee Growing Principle", "zh": "气液式雾化栽培系统 — 雾化咖啡种植原理", "ar": "نظام الزراعة الضبابية بالغاز والسائل — مبدأ زراعة القهوة الضبابية"},
    "bp2_desc": {"en": "This blueprint illustrates the patented gas-liquid atomization system: ultrasonic 1.7MHz atomizers generating 5-30μm nutrient mist, 300% more root oxygenation than deep-water hydroponics, closed-loop 90% water recovery, custom nutrient formulas per variety, gradient seedling hardening, and flowering induction achieving first harvest in 12-14 months — using only 2,100 L/kg water (vs. 21,000 L traditional).", "zh": "本蓝图展示了专利气液式雾化系统：超声波1.7MHz雾化器产生5-30μm营养雾滴，根系供氧量比深液流水培高300%，闭环水回收率90%，按品种定制营养液配方，梯度炼苗，以及开花诱导技术——12-14个月内首次收获，每公斤仅耗水2,100L（传统种植需21,000L）。", "ar": "يوضح هذا المخطط نظام الضبوب المسجل: مرذاذات فوق صوتية بتردد 1.7 ميجاهرتز تنتج قطرات ضباب مغذية 5-30 ميكرومتر، أكسجين جذور أعلى بنسبة 300% من الزراعة المائية العميقة، استرجاع مياه 90% في دورة مغلقة، تركيبات مغذية مخصصة لكل صنف، تقسية الشتلات المتدرجة، وتحفيز الإزهار المحقق لأول حصاد في 14-12 شهر — باستخدام 2,100 لتر/كجم فقط (مقارنة بـ 21,000 لتر للزراعة التقليدية)."},
    "bp2_caption": {"en": "FIG.1 Chamber Cross-Section | FIG.2 Ultrasonic Atomizer Detail | FIG.3 Closed-Loop Circulation | FIG.4 Root Oxygenation Comparison | FIG.5 Nutrient Formula & Growth Cycle | FIG.6 Water Efficiency Analysis", "zh": "图1 种植室截面 | 图2 超声波雾化器细节 | 图3 闭环循环 | 图4 根系供氧对比 | 图5 营养液配方与生长周期 | 图6 水效率分析", "ar": "شكل 1 مقطع غرفة الزراعة | شكل 2 تفاصيل المرذاذ فوق الصوتي | شكل 3 الدورة المغلقة | شكل 4 مقارنة أكسجين الجذور | شكل 5 تركيبة المغذيات ودورة النمو | شكل 6 تحليل كفاءة المياه"},
    "bp2_m1_lbl": {"en": "L/kg Water (vs 21,000 traditional)", "zh": "升/公斤水（传统21,000）", "ar": "لتر/كجم (مقابل 21,000 تقليدي)"},
    "bp2_m2_lbl": {"en": "Droplet Size Range", "zh": "雾滴尺寸范围", "ar": "نطاق حجم القطرات"},
    "bp2_m3_lbl": {"en": "Root Oxygenation vs DWC", "zh": "根系供氧 vs DWC", "ar": "أكسجين الجذور مقابل DWC"},
  },

  "drawings": {
    "sec_num": {"en": "Section 11", "zh": "第 11 节", "ar": "القسم 11"},
    "sec_title": {"en": "Technical Engineering Drawings", "zh": "技术工程图纸", "ar": "الرسومات الهندسية الفنية"},
    "sec_desc": {"en": "Complete system architecture, facility layout, value chain, and financial diagrams.", "zh": "完整的系统架构、设施布局、价值链和财务图表。", "ar": "رسومات كاملة لبنية النظام وتخطيط المنشأة وسلسلة القيمة والرسوم المالية."},
    "caption": {"en": "Figure 1-7: (1) Integrated Coffee Production System Architecture | (2) Vertical Coffee Farm Facility Layout — Saudi Deployment | (3) From Code to Cup — Full Value Chain | (4) Phased Implementation Roadmap | (5) Water Efficiency Comparison | (6) Financial Model & Projections | (7) PIF & Vision 2030 Strategic Alignment", "zh": "图1-7：(1) 集成咖啡生产系统架构 | (2) 垂直咖啡农场设施布局 — 沙特部署 | (3) 从代码到杯子 — 完整价值链 | (4) 分阶段实施路线图 | (5) 水效率对比 | (6) 财务模型与预测 | (7) PIF与愿景2030战略对齐", "ar": "شكل 1-7: (1) بنية نظام إنتاج القهوة المتكامل | (2) تخطيط مزرعة القهوة العمودية — نشر السعودي | (3) من الكود إلى الفنجان — سلسلة القيمة الكاملة | (4) خارطة طريق التنفيذ المرحلي | (5) مقارنة كفاءة المياه | (6) النموذج المالي والتوقعات | (7) التوافق الاستراتيجي PIF ورؤية 2030"},
    "notes_title": {"en": "Technical Drawing Notes", "zh": "技术图纸说明", "ar": "ملاحظات الرسومات الفنية"},
    "notes_text": {"en": "The above engineering drawings illustrate the complete system architecture for Saudi deployment. <strong>Diagram 1</strong> shows the three-layer technology stack: AI robotic tissue culture (Layer 1), gas-liquid atomization hydroponic system (Layer 2, the patented core), and closed-loop water/nutrient circuit. <strong>Diagram 2</strong> provides the facility layout for a 50,000 m² controlled-environment farm — four zones with 4-level vertical stacking achieving 48,000 m² effective growing area. <strong>Diagram 3</strong> maps the full value chain from genetic bank to retail. <strong>Diagram 5</strong> demonstrates the critical water efficiency advantage (2,100 L/kg vs 21,000 L/kg) that makes this technology uniquely viable for Saudi Arabia's water-scarce environment.", "zh": "以上工程图纸展示了沙特部署的完整系统架构。<strong>图1</strong>展示三层技术堆栈：AI机器人组培（第一层）、气液式雾化水培系统（第二层，专利核心）和闭环水/营养液回路。<strong>图2</strong>提供50,000 m²受控环境农场的设施布局——四区四层垂直堆叠，实现48,000 m²有效种植面积。<strong>图3</strong>绘制从基因库到零售的完整价值链。<strong>图5</strong>展示关键水效率优势（2,100升/公斤 vs 21,000升/公斤），使该技术独特地适用于沙特水资源稀缺环境。", "ar": "توضح الرسومات الهندسية أعلاه بنية النظام الكامل للنشر السعودي. <strong>الرسم 1</strong> يعرض مكدس التقنية ثلاثي الطبقات: زراعة الأنسجة بالروبوت الذكي (الطبقة 1)، نظام الزراعة المائية الضبابية (الطبقة 2، النواة المسجلة)، ودائرة المياه/المغذيات المغلقة. <strong>الرسم 2</strong> يوفر تخطيط المنشأة لمزرعة بيئة محكومة 50,000 م² — أربع مناطق برصف عمودي 4 مستويات محققاً 48,000 م² مساحة زراعة فعالة. <strong>الرسم 3</strong> يرسم سلسلة القيمة الكاملة من البنك الجيني إلى التجزئة. <strong>الرسم 5</strong> يوضح ميزة كفاءة المياه الحرجة (2,100 لتر/كجم مقابل 21,000 لتر/كجم) التي تجعل هذه التقنية قابلة للتطبيق بشكل فريد في بيئة السعودية المحدودة المياه."},
  },

  "video": {
    "sec_num": {"en": "Section 12", "zh": "第 12 节", "ar": "القسم 12"},
    "sec_title": {"en": "Video Brief — El Niño 2026 &amp; the Aeroponic Answer", "zh": "视频简报 — 2026 厄尔尼诺与气雾栽培答案", "ar": "فيديو توضيحي — إلنينو 2026 وجواب الضبوب"},
    "sec_desc": {"en": "A 68-second climate intelligence briefing produced by Napell BIO — connecting the global El Niño 2026 crisis to the aeroponic solution and the Saudi opportunity.", "zh": "Napell BIO 出品的 68 秒气候情报简报，将全球 2026 厄尔尼诺危机与气雾栽培解决方案及沙特机遇串联。", "ar": "موجز استخبارات مناخي مدته 68 ثانية أنتجته Napell BIO — يربط أزمة إلنينو 2026 العالمية بحلول الضبوب وفرصة السعودية."},
    "video_label": {"en": "Watch Briefing", "zh": "观看简报", "ar": "شاهد الموجز"},
    "video_sublabel": {"en": "68 seconds · 1080p · Mandarin narration with on-screen text in EN/中文/العربية", "zh": "68 秒 · 1080p · 中文解说配 EN/中文/العربية 三语字幕", "ar": "68 ثانية · 1080 بكسل · سرد صيني مع نص على الشاشة بـ EN/中文/العربية"},
    "no_video_warning": {"en": "Your browser does not support embedded video. Download it instead:", "zh": "您的浏览器不支持嵌入视频。请改用下载链接：", "ar": "متصفحك لا يدعم الفيديو المضمّن. حمّله بدلاً من ذلك:"},
    "download_btn": {"en": "Download MP4 (8.2 MB)", "zh": "下载 MP4 (8.2 MB)", "ar": "تحميل MP4 (8.2 ميجابايت)"},
    "analysis_title": {"en": "Why This Video Matters to the Saudi Coffee Chain", "zh": "为什么这段视频对沙特咖啡链至关重要", "ar": "لماذا هذا الفيديو مهم لسلسلة القهوة السعودية"},
    "analysis_intro": {"en": "This briefing distills the strategic case in 68 seconds. It is a market-reality video — not a product demo — designed to anchor the conversation between Napell and PIF in three layers of evidence:", "zh": "这段简报在 68 秒内浓缩了整个战略论证。它不是产品演示，而是一段\"市场现实\"视频，旨在为 Napell 与 PIF 的对话锚定三层证据：", "ar": "يلخص هذا الموجز القضية الاستراتيجية في 68 ثانية. إنه فيديو واقع السوق — وليس عرض منتج — مصمم لتأسيس المحادثة بين Napell وصندوق PIF على ثلاث طبقات من الأدلة:"},
    "layer1_title": {"en": "Layer 1 — The Threat is Real, Quantified, and Accelerating", "zh": "第一层 — 威胁是真实、量化且加速的", "ar": "الطبقة 1 — التهديد حقيقي ومحدد كمياً ومتسارع"},
    "layer1_text": {"en": "Using data sourced from the International Coffee Organization (ICO), World Coffee Research, and NOAA's 2026 climate forecast, the video quantifies the 2026 El Niño impact: +2.8°C mean temperature increase, –38% rainfall deficit, and 24% loss of coffee planting area. Global production is projected to fall 37% (from 98M bags in 2022 to 62M in 2026P), while Arabica futures prices are projected to surge 293% (from $1.22/lb in 2020 to $4.80 in 2026P). Four flagship origins — Brazil, Colombia, Vietnam, Ethiopia — are shown to be at severe-to-extreme risk. The video further cites ICO's projection that <strong>50% of global coffee arable land will disappear by 2050</strong>, directly threatening 120 million livelihoods.", "zh": "使用国际咖啡组织（ICO）、世界咖啡研究及 NOAA 2026 气候预测的数据，影片量化了 2026 厄尔尼诺的影响：均温上升 +2.8°C、降雨缺口 –38%、咖啡种植面积减少 24%。全球产量预计下降 37%（从 2022 年的 9800 万袋降至 2026P 的 6200 万袋），阿拉伯卡咖啡期货价格预计飙升 293%（从 2020 年的 $1.22/磅升至 2026P 的 $4.80）。巴西、哥伦比亚、越南、埃塞俄比亚四大旗舰产地均被标注为重度至极度风险。影片进一步引用 ICO 的预测——<strong>到 2050 年全球 50% 的咖啡可耕种土地将消失</strong>，直接威胁 1.2 亿人的生计。", "ar": "باستخدام بيانات من المنظمة الدولية للقهوة (ICO) وبحوث القهوة العالمية وتوقعات NOAA المناخية لعام 2026، يحدد الفيديو تأثير إلنينو 2026: +2.8°C ارتفاع في متوسط الحرارة، –38% عجز في الأمطار، و24% فقدان في مساحة زراعة القهوة. من المتوقع أن ينخفض الإنتاج العالمي بنسبة 37% (من 98 مليون كيس في 2022 إلى 62 مليوناً في 2026P)، بينما من المتوقع أن ترتفع أسعار العقود الآجلة للأرابيكا بنسبة 293% (من 1.22 دولار/رطل في 2020 إلى 4.80 دولار في 2026P). تُظهر الأصول الأربعة الرئيسية — البرازيل وكولومبيا وفيتنام وإثيوبيا — على أنها في خطر شديد إلى متطرف. يستشهد الفيديو كذلك بتوقعات ICO بأن <strong>50% من الأراضي الصالحة لزراعة القهوة عالمياً ستختفي بحلول عام 2050</strong>، مما يهدد مباشرة سبل عيش 120 مليون شخص."},
    "layer2_title": {"en": "Layer 2 — Traditional Soil Cultivation Cannot Survive This", "zh": "第二层 — 传统土壤种植无法承受这一切", "ar": "الطبقة 2 — الزراعة التقليدية في التربة لا يمكنها البقاء"},
    "layer2_text": {"en": "The video identifies three systemic vulnerabilities that traditional soil farming cannot mitigate: (1) <strong>Climate fragility</strong> — coffee requires 1,500–2,000mm stable rainfall and 18–24°C temperatures; El Niño breaks both, triggering a 65% surge in crop pests/diseases. (2) <strong>Water waste &amp; soil degradation</strong> — soil-grown coffee consumes up to 140 liters of water per cup and loses 35% of topsoil per decade. (3) <strong>Pest outbreak pressure</strong> — coffee leaf rust and coffee berry borer spread 55% faster under El Niño conditions, with soil farms having no isolation barrier, causing up to 50% yield losses and $340/ha extra pesticide cost.", "zh": "视频指出了传统土壤种植无法缓解的三个系统性脆弱环节：(1) <strong>气候脆弱性</strong>——咖啡需要 1,500–2,000mm 稳定降雨和 18–24°C 温度；厄尔尼诺打破两者，导致作物病虫害激增 65%。(2) <strong>水资源浪费与土壤退化</strong>——土壤种植咖啡每杯耗水高达 140 升，每十年表土流失 35%。(3) <strong>病虫害暴发压力</strong>——咖啡叶锈病和咖啡果小蠹在厄尔尼诺条件下传播速度加快 55%，土壤种植无隔离屏障，导致高达 50% 的产量损失和每公顷 $340 的额外农药成本。", "ar": "يحدد الفيديو ثلاث ثغرات منهجية لا يمكن للزراعة التقليدية في التربة التخفيف منها: (1) <strong>الهشاشة المناخية</strong> — تتطلب القهوة 1,500–2,000 ملم من الأمطار المستقرة ودرجات حرارة 18–24°C؛ يكسر إلنينو كليهما، مما يؤدي إلى زيادة 65% في آفات وأمراض المحاصيل. (2) <strong>هدر المياه وتدهور التربة</strong> — تستهلك القهوة المزروعة في التربة ما يصل إلى 140 لتراً من الماء لكل كوب وتفقد 35% من الطبقة السطحية كل عقد. (3) <strong>ضغط تفشي الآفات</strong> — ينتشر صدأ أوراق القهوة وسوسة حبة القهوة بسرعة 55% في ظروف إلنينو، بدون حواجز عزل في مزارع التربة، مما يتسبب في خسائر إنتاج تصل إلى 50% وتكلفة مبيدات إضافية قدرها 340 دولار/هكتار."},
    "layer3_title": {"en": "Layer 3 — Aeroponics is the Only Defensible Answer", "zh": "第三层 — 气雾栽培是唯一可防御的答案", "ar": "الطبقة 3 — الضبوب هي الجواب الوحيد القابل للدفاع"},
    "layer3_text": {"en": "The video closes with Napell BIO's aeroponic system delivering three structural wins: <strong>95% water reduction</strong> vs soil (root misting has no runoff), <strong>365-day uninterrupted production</strong> in fully climate-controlled 20–22°C vertical towers with 1,600 lux lighting, and <strong>3× growth speed</strong> via oxygen-rich nutrient mist that accelerates mineral uptake. The harvest cycle drops from 4 years to 12–14 months. This is precisely why Saudi Arabia — with its 2.4B m³ renewable water ceiling and Vision 2030 food-security mandate — is the highest-leverage geography in the world for this technology.", "zh": "视频以 Napell BIO 的气雾栽培系统实现的三项结构性胜利结尾：<strong>节水 95%</strong>（根系雾化无径流）、<strong>365 天不间断生产</strong>（20–22°C 全气候可控垂直塔，1,600 lux 光照）、<strong>生长速度 3 倍</strong>（富氧营养雾加速矿物质吸收）。收获周期从 4 年缩短至 12–14 个月。这正是为什么沙特阿拉伯——拥有 24 亿立方米可再生水上限和愿景 2030 粮食安全使命——是全球该技术最高杠杆的地理选择。", "ar": "يختتم الفيديو بفوز هيكلي ثلاثي لنظام الضبوب من Napell BIO: <strong>تخفيض 95% من المياه</strong> مقابل التربة (ضباب الجذور بدون جريان)، <strong>إنتاج متواصل 365 يوماً</strong> في أبراج عمودية مكيفة المناخ بالكامل 20–22°C بإضاءة 1,600 لوكس، و<strong>سرعة نمو 3 أضعاف</strong> عبر ضباب المغذيات الغني بالأكسجين الذي يسرع امتصاص المعادن. تنخفض دورة الحصاد من 4 سنوات إلى 12–14 شهراً. هذا هو بالضبط السبب الذي يجعل السعودية — بسقف 2.4 مليار م³ من المياه المتجددة وتفويض رؤية 2030 للأمن الغذائي — أعلى جغرافيا رافعة في العالم لهذه التقنية."},
    "inv_title": {"en": "Implications for the Saudi Arabia Investment Thesis", "zh": "对沙特阿拉伯投资论点的影响", "ar": "تداعيات على فرضية الاستثمار في المملكة العربية السعودية"},
    "inv1": {"en": "Time compression — Saudi cannot wait 25 years for traditional farms to be retrofitted. The El Niño crisis is <strong>now</strong>. Aeroponics is the only path to sovereign coffee security in this decade.", "zh": "时间压缩——沙特等不了 25 年来改造传统农场。厄尔尼诺危机<strong>现在</strong>已发生。气雾栽培是本十年内实现主权咖啡安全的唯一路径。", "ar": "ضغط الوقت — لا تستطيع السعودية الانتظار 25 عاماً لتحديث المزارع التقليدية. أزمة إلنينو <strong>الآن</strong>. الضبوب هي المسار الوحيد للأمن السيادي للقهوة في هذا العقد."},
    "inv2": {"en": "Price tailwind — at projected $4.80/lb Arabica and tightening supply, every ton Napell produces in Saudi is sold into a structural bull market, accelerating the JV's path to breakeven.", "zh": "价格顺风——按预计 $4.80/磅的阿拉伯卡价格和日益紧张的供应，Napell 在沙特每生产一吨咖啡都进入结构性牛市，加速合资企业盈亏平衡之路。", "ar": "رياح الأسعار المؤاتية — عند 4.80 دولار/رطل المتوقعة للأرابيكا والمعروض المشدد، كل طن تنتجه Napell في السعودية يُباع في سوق صاعد هيكلي، مما يسرع مسار المشروع المشترك نحو نقطة التعادل."},
    "inv3": {"en": "Strategic optionality — PIF's investment de-risks Vision 2030's food-security pillar while capturing a defensible position in the global indoor-coffee technology stack that no other Gulf sovereign is positioned to take.", "zh": "战略期权——PIF 的投资既降低了愿景 2030 粮食安全支柱的风险，又在全球室内咖啡技术栈中占据了一个任何其他海湾主权国家都无法抢占的防御性位置。", "ar": "الاختيارية الاستراتيجية — استثمار PIF يُقلل من مخاطر ركيزة الأمن الغذائي لرؤية 2030 بينما يلتقط موقعاً دفاعياً في مكدس تقنية القهوة الداخلية العالمية التي لا يوجد أي سيادي خليجي آخر في وضع يسمح له بأخذها."},
    "transcript_title": {"en": "On-screen Text &amp; Data (Key Frames)", "zh": "屏幕文字与数据（关键帧）", "ar": "النص والبيانات على الشاشة (الإطارات الرئيسية)"},
    "transcript_t0_5": {"en": "Opening — Napell BIO logo + tagline: <em>\"Growing the future, today\"</em>", "zh": "开场 — Napell BIO 标志 + 标语：<em>\"今天，播种未来\"</em>", "ar": "الافتتاح — شعار Napell BIO + الشعار: <em>\"اليوم، نزرع المستقبل\"</em>"},
    "transcript_t10": {"en": "Title — <em>\"EL NIÑO 2026 → COFFEE CRISIS\"</em>. Subtitle in English: <em>\"How the world's most extreme El Niño threatens global coffee supply, and the aeroponic technology changing everything\"</em>.", "zh": "标题 — <em>\"2026 厄尔尼诺 → 咖啡危机\"</em>。英文副标题：<em>\"史上最强厄尔尼诺如何威胁全球咖啡供应，气雾栽培技术正在改写一切\"</em>。", "ar": "العنوان — <em>\"إلنينو 2026 ← أزمة القهوة\"</em>. العنوان الفرعي بالإنجليزية: <em>\"كيف يهدد أقوى إلنينو في العالم إمدادات القهوة العالمية، وكيف تغير تقنية الضبوب كل شيء\"</em>."},
    "transcript_t15": {"en": "Section — <em>\"Top coffee origins face severe threats\"</em>: Brazil 88% risk, Colombia 74%, Vietnam 92%, Ethiopia 68%. Headline stats: +2.8°C, –38% rainfall, 24% planting area lost.", "zh": "章节 — <em>\"全球顶级咖啡产区面临严重威胁\"</em>：巴西 88% 风险、哥伦比亚 74%、越南 92%、埃塞俄比亚 68%。头条数据：+2.8°C、–38% 降雨、24% 种植面积消失。", "ar": "القسم — <em>\"أصول القهوة الرئيسية العالمية تواجه تهديدات شديدة\"</em>: البرازيل 88% خطر، كولومبيا 74%، فيتنام 92%، إثيوبيا 68%. إحصائيات رئيسية: +2.8°C، –38% أمطار، 24% مساحة زراعة ضائعة."},
    "transcript_t25": {"en": "Section — <em>\"Supply shock &amp; price surge\"</em>: Global production –37% (98M → 62M bags, 2022 → 2026P); Arabica futures +293% ($1.22 → $4.80/lb, 2020 → 2026P). Source: ICO + WCR + NOAA.", "zh": "章节 — <em>\"供应冲击与价格飙升\"</em>：全球产量 –37%（98M → 62M 袋，2022 → 2026P）；阿拉伯卡期货 +293%（$1.22 → $4.80/磅，2020 → 2026P）。数据源：ICO + WCR + NOAA。", "ar": "القسم — <em>\"صدمة المعروض وارتفاع الأسعار\"</em>: الإنتاج العالمي –37% (98 مليون ← 62 مليون كيس، 2022 ← 2026P)؛ عقود الأرابيكا الآجلة +293% (1.22 ← 4.80 دولار/رطل، 2020 ← 2026P). المصدر: ICO + WCR + NOAA."},
    "transcript_t35": {"en": "Section — <em>\"Coffee arable land will shrink 50% by 2050\"</em>. Source: ICO.", "zh": "章节 — <em>\"到 2050 年咖啡可耕种土地将减少 50%\"</em>。数据源：ICO。", "ar": "القسم — <em>\"ستنخفض الأراضي الصالحة لزراعة القهوة بنسبة 50% بحلول 2050\"</em>. المصدر: ICO."},
    "transcript_t40": {"en": "Section — <em>\"3 systemic vulnerabilities\"</em>: ① Climate fragility (1,500–2,000mm rain &amp; 18–24°C required; +65% pest surge). ② Water waste &amp; soil degradation (140L water per cup; 35% topsoil loss/decade). ③ Pest outbreak pressure (+55% leaf rust; +$340/ha pesticide cost; up to 50% yield loss).", "zh": "章节 — <em>\"三大系统性脆弱环节\"</em>：① 气候脆弱性（需 1,500–2,000mm 降雨 &amp; 18–24°C；病虫害激增 65%）。② 水资源浪费与土壤退化（每杯耗水 140 升；每十年表土流失 35%）。③ 病虫害暴发压力（叶锈病 +55%；每公顷额外农药成本 +$340；高达 50% 产量损失）。", "ar": "القسم — <em>\"3 ثغرات منهجية\"</em>: ① الهشاشة المناخية (1,500–2,000 ملم أمطار &amp; 18–24°C مطلوبة؛ +65% ارتفاع في الآفات). ② هدر المياه وتدهور التربة (140 لتر/كوب؛ 35% فقدان تربة سطحية/عقد). ③ ضغط تفشي الآفات (+55% صدأ الأوراق؛ +340 دولار/هكتار تكلفة مبيدات؛ حتى 50% خسارة إنتاج)."},
    "transcript_t55": {"en": "Section — <em>\"Aeroponic Coffee Cultivation System\"</em>: 95% water saving, 365-day uninterrupted production, 3× growth speed, harvest cycle 4 yr → 12–14 mo.", "zh": "章节 — <em>\"气雾栽培咖啡种植系统\"</em>：节水 95%、365 天不间断生产、生长速度 3 倍、收获周期 4 年 → 12–14 个月。", "ar": "القسم — <em>\"نظام زراعة القهوة بالضبوب\"</em>: توفير 95% من المياه، إنتاج متواصل 365 يوماً، سرعة نمو 3 أضعاف، دورة حصاد 4 سنوات ← 12–14 شهراً."},
    "transcript_t65": {"en": "Closing — Napell BIO + <em>\"Growing the future, today\"</em>. Two closing messages: (1) 2026 Super El Niño is disrupting the global coffee supply chain. (2) Traditional soil cultivation cannot withstand extreme climate shocks.", "zh": "结尾 — Napell BIO + <em>\"今天，播种未来\"</em>。两条收尾信息：(1) 2026 超级厄尔尼诺正在扰乱全球咖啡供应链。(2) 传统土壤种植无法承受极端气候冲击。", "ar": "الختام — Napell BIO + <em>\"اليوم، نزرع المستقبل\"</em>. رسالتان ختاميتان: (1) إلنينو 2026 الفائق يعطل سلسلة إمداد القهوة العالمية. (2) الزراعة التقليدية في التربة لا يمكنها تحمل صدمات المناخ المتطرف."},
    "use_title": {"en": "How to Use This Video with PIF", "zh": "如何向 PIF 展示本视频", "ar": "كيفية استخدام هذا الفيديو مع PIF"},
    "use1": {"en": "<strong>Open the meeting</strong> with the 68-second briefing — it sets the urgency frame in under two minutes and reaches the C-suite without a slide deck.", "zh": "<strong>开场播放</strong>——用 68 秒简报开场，两分钟内在没有幻灯片的情况下向高管层传达紧迫感。", "ar": "<strong>افتتح الاجتماع</strong> بالموجز الذي مدته 68 ثانية — يحدد إطار الإلحاح في أقل من دقيقتين ويصل إلى الإدارة العليا بدون شرائح."},
    "use2": {"en": "<strong>Anchor the data</strong> by linking to the source citations (ICO, NOAA, WCR) shown in the closing frames — PIF analysts can verify independently.", "zh": "<strong>锚定数据</strong>——通过视频结尾处显示的来源引用（ICO、NOAA、WCR），PIF 分析师可独立验证。", "ar": "<strong>ربط البيانات</strong> بالإشارة إلى المصادر (ICO، NOAA، WCR) المعروضة في الإطارات الختامية — يمكن لمحللـي PIF التحقق بشكل مستقل."},
    "use3": {"en": "<strong>Hand off</strong> to Section 04 (Market) and Section 02 (Context) of this proposal for the full financial and strategic depth — the video is the hook, the proposal is the close.", "zh": "<strong>接力</strong>至本提案第 4 节（市场）和第 2 节（背景）以获取完整财务与战略深度——视频是钩子，提案是收单。", "ar": "<strong>سلّم</strong> إلى القسم 04 (السوق) والقسم 02 (السياق) من هذا العرض للعمق المالي والاستراتيجي الكامل — الفيديو هو الطُعم، والعرض هو الإغلاق."},
  },

  "contact": {
    "sec_num": {"en": "Next Steps", "zh": "下一步", "ar": "الخطوات التالية"},
    "sec_title": {"en": "Let's Build Saudi Arabia's Coffee Future", "zh": "让我们建设沙特阿拉伯的咖啡未来", "ar": "لنبني مستقبل القهوة في السعودية"},
    "sec_desc": {"en": "We are ready to present this proposal in person and begin the due diligence process.", "zh": "我们随时准备亲自提交此提案并开始尽职调查。", "ar": "نحن مستعدون لتقديم هذا العرض شخصياً وبدء عملية العناية الواجبة."},
    "s1_title": {"en": "Step 1", "zh": "步骤一", "ar": "الخطوة 1"},
    "s1_name": {"en": "Initial Meeting", "zh": "初步会议", "ar": "اجتماع أولي"},
    "s1_desc": {"en": "Present full proposal to PIF investment team. Technology demo video and live Q&A.", "zh": "向PIF投资团队提交完整提案。技术演示视频和现场问答。", "ar": "تقديم العرض الكامل لفريق استثمار PIF. فيديو عرض تقني وأسئلة وأجوبة مباشرة."},
    "s2_title": {"en": "Step 2", "zh": "步骤二", "ar": "الخطوة 2"},
    "s2_name": {"en": "Technical Due Diligence", "zh": "技术尽职调查", "ar": "العناية الواجبة الفنية"},
    "s2_desc": {"en": "Site visit to existing facilities. Technology validation. Patent review.", "zh": "参观现有设施。技术验证。专利审查。", "ar": "زيارة الموقع للمنشآت القائمة. التحقق من التقنية. مراجعة براءة الاختراع."},
    "s3_title": {"en": "Step 3", "zh": "步骤三", "ar": "الخطوة 3"},
    "s3_name": {"en": "Term Sheet", "zh": "条款清单", "ar": "ورقة الشروط"},
    "s3_desc": {"en": "JV structure, investment schedule, IP licensing terms, governance framework.", "zh": "合资结构、投资计划、IP授权条款、治理框架。", "ar": "هيكل المشروع المشترك، جدول الاستثمار، شروط ترخيص الملكية الفكرية، إطار الحوكمة."},
    "contact_title": {"en": "Contact Napell Biotech", "zh": "联系 Napell Biotech", "ar": "تواصل مع Napell Biotech"},
    "contact_ref": {"en": "Patent Reference: CN 202611094298.6 &nbsp;|&nbsp; Proposal Date: July 2026", "zh": "专利参考: CN 202611094298.6 &nbsp;|&nbsp; 提案日期: 2026年7月", "ar": "مرجع براءة الاختراع: CN 202611094298.6 &nbsp;|&nbsp; تاريخ العرض: يوليو 2026"},
  }
}

# ============================================================
# Generate i18n.js
# ============================================================
def gen_i18n_js():
    lines = [
        "// Auto-generated trilingual translations (EN / 中文 / العربية)",
        "const I18N = " + json.dumps(T, ensure_ascii=False, indent=2) + ";",
        "",
        "function getLang() {",
        "  return localStorage.getItem('lang') || 'en';",
        "}",
        "",
        "function setLang(lang) {",
        "  localStorage.setItem('lang', lang);",
        "  document.documentElement.lang = lang;",
        "  document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';",
        "  document.querySelectorAll('.lang-btn').forEach(btn => {",
        "    btn.classList.toggle('active', btn.dataset.lang === lang);",
        "  });",
        "  document.querySelectorAll('[data-i18n]').forEach(el => {",
        "    const key = el.getAttribute('data-i18n');",
        "    const parts = key.split('.');",
        "    let val = I18N;",
        "    for (const p of parts) {",
        "      if (val && val[p]) val = val[p];",
        "      else { val = null; break; }",
        "    }",
        "    if (val && val[lang]) {",
        "      el.innerHTML = val[lang];",
        "    }",
        "  });",
        "  // Update chart labels if charts exist",
        "  if (typeof updateChartLabels === 'function') updateChartLabels(lang);",
        "}",
        "",
        "document.addEventListener('DOMContentLoaded', () => {",
        "  setLang(getLang());",
        "});",
    ]
    return '\n'.join(lines)

# ============================================================
# HTML Template
# ============================================================
NAV_HTML = """<nav>
  <a href="index.html" class="logo" data-i18n="common.logo">PIF × NAPELL</a>
  <ul class="nav-links">
    <li class="nav-dropdown">
      <a href="index.html" data-i18n="common.nav_summary">Summary</a>
      <div class="dropdown-menu">
        <a href="index.html" data-i18n="common.dd_summary_exec">Executive Summary</a>
        <a href="index.html" data-i18n="common.dd_summary_metrics">Key Market Metrics</a>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="context.html" data-i18n="common.nav_context">Context</a>
      <div class="dropdown-menu">
        <a href="context.html" data-i18n="common.dd_context_vision">Vision 2030 Mandate</a>
        <a href="context.html" data-i18n="common.dd_context_import">Market Import Volume</a>
        <a href="context.html" data-i18n="common.dd_context_water">Water Scarcity Crisis</a>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="video.html" data-i18n="common.nav_video">El Niño</a>
      <div class="dropdown-menu">
        <a href="video.html" data-i18n="common.dd_video_crisis">El Niño 2026 Coffee Crisis</a>
        <a href="video.html" data-i18n="common.dd_video_solution">Aeroponic Solution</a>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="technology.html" data-i18n="common.nav_technology">Technology</a>
      <div class="dropdown-menu">
        <a href="technology.html" data-i18n="common.dd_tech_patent">Patent CN 202611094298.6</a>
        <a href="blueprints.html" data-i18n="common.dd_tech_robotic">AI Robotic Tissue Culture</a>
        <a href="blueprints.html" data-i18n="common.dd_tech_aeroponic">Atomization Hydroponics</a>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="market.html" data-i18n="common.nav_market">Market</a>
      <div class="dropdown-menu">
        <a href="market.html" data-i18n="common.dd_market_size">Market Size &amp; Growth</a>
        <a href="market.html" data-i18n="common.dd_market_sub">Import Substitution</a>
        <a href="market.html" data-i18n="common.dd_market_charts">Growth Charts</a>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="proposal.html" data-i18n="common.nav_proposal">Proposal</a>
      <div class="dropdown-menu">
        <a href="proposal.html" data-i18n="common.dd_prop_pif">PIF Contribution</a>
        <a href="proposal.html" data-i18n="common.dd_prop_napell">Napell Contribution</a>
        <a href="proposal.html" data-i18n="common.dd_prop_jv">JV Structure</a>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="roadmap.html" data-i18n="common.nav_roadmap">Roadmap</a>
      <div class="dropdown-menu">
        <a href="roadmap.html" data-i18n="common.dd_road_1">Phase 1: Pilot Farm</a>
        <a href="roadmap.html" data-i18n="common.dd_road_2">Phase 2: Commercial Scale</a>
        <a href="roadmap.html" data-i18n="common.dd_road_3">Phase 3: National Scale</a>
        <a href="roadmap.html" data-i18n="common.dd_road_4">Phase 4: Global Brand</a>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="financials.html" data-i18n="common.nav_financials">Financials</a>
      <div class="dropdown-menu">
        <a href="financials.html" data-i18n="common.dd_fin_invest">Investment Allocation</a>
        <a href="financials.html" data-i18n="common.dd_fin_pl">P&amp;L Summary</a>
        <a href="financials.html" data-i18n="common.dd_fin_roi">ROI Metrics</a>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="risks.html" data-i18n="common.nav_risks">Risks</a>
    </li>
    <li class="nav-dropdown">
      <a href="alignment.html" data-i18n="common.nav_alignment">Alignment</a>
    </li>
    <li class="nav-dropdown">
      <a href="blueprints.html" data-i18n="common.nav_blueprints">Blueprints</a>
      <div class="dropdown-menu">
        <a href="blueprints.html" data-i18n="common.dd_bp_robotic">Robotic Arm Blueprint</a>
        <a href="blueprints.html" data-i18n="common.dd_bp_aeroponic">Aeroponic System Blueprint</a>
        <a href="drawings.html" data-i18n="common.dd_drawings_system">System Architecture</a>
        <a href="drawings.html" data-i18n="common.dd_drawings_facility">Facility Layout</a>
      </div>
    </li>
  </ul>
  <div class="nav-right">
    <div class="lang-switcher">
      <button class="lang-btn active" data-lang="en" onclick="setLang('en')">EN</button>
      <button class="lang-btn" data-lang="zh" onclick="setLang('zh')">中文</button>
      <button class="lang-btn" data-lang="ar" onclick="setLang('ar')">العربية</button>
    </div>
    <a href="contact.html" class="nav-cta" data-i18n="common.nav_connect">Connect</a>
  </div>
  <button class="hamburger" id="hamburger" aria-label="Menu" onclick="toggleMobileMenu()">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="mobile-menu" id="mobileMenu">
  <a href="index.html" data-i18n="common.nav_summary">Summary</a>
  <a href="context.html" data-i18n="common.nav_context">Context</a>
  <a href="video.html" data-i18n="common.nav_video">El Niño</a>
  <a href="technology.html" data-i18n="common.nav_technology">Technology</a>
  <a href="market.html" data-i18n="common.nav_market">Market</a>
  <a href="proposal.html" data-i18n="common.nav_proposal">Proposal</a>
  <a href="roadmap.html" data-i18n="common.nav_roadmap">Roadmap</a>
  <a href="financials.html" data-i18n="common.nav_financials">Financials</a>
  <a href="risks.html" data-i18n="common.nav_risks">Risks</a>
  <a href="alignment.html" data-i18n="common.nav_alignment">Alignment</a>
  <a href="blueprints.html" data-i18n="common.nav_blueprints">Blueprints</a>
  <a href="drawings.html" data-i18n="common.nav_drawings">Drawings</a>
  <a href="contact.html" class="mobile-cta" data-i18n="common.nav_connect">Connect</a>
  <div class="mobile-lang-switcher">
    <button class="lang-btn active" data-lang="en" onclick="setLang('en')">EN</button>
    <button class="lang-btn" data-lang="zh" onclick="setLang('zh')">中文</button>
    <button class="lang-btn" data-lang="ar" onclick="setLang('ar')">العربية</button>
  </div>
</div>
<div class="mobile-overlay" id="mobileOverlay" onclick="toggleMobileMenu()"></div>"""

FOOTER_HTML = """<footer>
  <p data-i18n="common.footer_rights">Napell Biotech (Hong Kong) Ltd. — All Rights Reserved.</p>
  <p style="margin-top:8px" data-i18n="common.footer_patent">Patent: CN 202611094298.6 — Gas-Liquid Atomization Based Full-Cycle Planting Management Method & System</p>
  <p style="margin-top:8px" data-i18n="common.footer_confidential">This document is confidential and intended solely for the Public Investment Fund (PIF) of the Kingdom of Saudi Arabia.</p>
</footer>"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="css/styles.css">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
</head>
<body>
{nav}
"""

TAIL = """
{footer}
<script src="js/i18n.js"></script>
<script src="js/main.js"></script>
</body>
</html>"""

# ============================================================
# Page Content
# ============================================================
def page_index():
    body = """<section class="hero">
  <div class="confidential" data-i18n="index.confidential">Confidential — For PIF Review Only</div>
  <h1 data-i18n="index.title">Building Saudi Arabia's<br> Sovereign Coffee Industry Chain</h1>
  <p class="subtitle" data-i18n="index.subtitle">A strategic partnership proposal leveraging proprietary AI-robotic tissue culture and gas-liquid atomization hydroponic technology to establish a fully integrated, climate-resilient coffee production ecosystem in the Kingdom of Saudi Arabia.</p>
  <div class="meta">
    <span data-i18n="index.meta_prepared">Prepared by: Napell Biotech (Hong Kong) Ltd.</span>
    <span data-i18n="index.meta_date">Date: July 2026</span>
    <span data-i18n="index.meta_ref">Ref: Patent CN 202611094298.6</span>
  </div>
</section>

<section class="section" id="summary">
  <div class="section-header">
    <div class="num" data-i18n="index.sec_num">Section 01</div>
    <h2 data-i18n="index.sec_title">Executive Summary</h2>
    <p data-i18n="index.sec_desc">The opportunity, the technology, and why PIF should act now.</p>
  </div>
  <div class="data-row">
    <div class="data-item"><div class="value" style="color:var(--accent)" data-i18n="index.m1_val">$900B+</div><div class="label" data-i18n="index.m1_lbl">PIF Assets Under Management (2026)</div></div>
    <div class="data-item"><div class="value" style="color:var(--green)" data-i18n="index.m2_val">SAR 5-7B</div><div class="label" data-i18n="index.m2_lbl">Saudi Coffee Market Value (2024)</div></div>
    <div class="data-item"><div class="value" style="color:var(--orange)" data-i18n="index.m3_val">80,000+</div><div class="label" data-i18n="index.m3_lbl">Tons Coffee Consumed Annually (Saudi)</div></div>
    <div class="data-item"><div class="value" style="color:var(--red)" data-i18n="index.m4_val">~96%</div><div class="label" data-i18n="index.m4_lbl">Import Dependency Rate</div></div>
  </div>
  <div class="card" style="margin-top:32px">
    <p style="font-size:16px;line-height:1.8" data-i18n="index.p1"></p>
    <p style="font-size:16px;line-height:1.8;margin-top:16px" data-i18n="index.p2"></p>
    <p style="font-size:16px;line-height:1.8;margin-top:16px" data-i18n="index.p3"></p>
  </div>
</section>"""
    return HEAD.format(title="PIF × NAPELL — Saudi Coffee Industry Chain Proposal", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

def page_context():
    body = """<section class="section">
  <div class="section-header">
    <div class="num" data-i18n="context.sec_num">Section 02</div>
    <h2 data-i18n="context.sec_title">Strategic Context</h2>
    <p data-i18n="context.sec_desc">Why Saudi Arabia needs sovereign coffee production — and why now.</p>
  </div>
  <div class="card-grid col3">
    <div class="card"><h3 style="color:var(--accent)" data-i18n="context.c1_title">Vision 2030 Mandate</h3><p data-i18n="context.c1_text"></p></div>
    <div class="card"><h3 style="color:var(--green)" data-i18n="context.c2_title">Market Import Volume</h3><p data-i18n="context.c2_text"></p></div>
    <div class="card"><h3 style="color:var(--purple)" data-i18n="context.c3_title">Water Scarcity Crisis</h3><p data-i18n="context.c3_text"></p></div>
  </div>
  <div class="card" style="margin-top:24px;border-left:3px solid var(--accent)">
    <p style="font-size:15px;line-height:1.8;color:var(--text-secondary)">
      <strong style="color:var(--text-primary)" data-i18n="context.insight_label">Key Insight:</strong>
      <span data-i18n="context.insight_text"></span>
    </p>
  </div>
</section>"""
    return HEAD.format(title="Strategic Context — PIF × NAPELL", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

def page_technology():
    body = """<section class="section">
  <div class="section-header">
    <div class="num" data-i18n="technology.sec_num">Section 03</div>
    <h2 data-i18n="technology.sec_title">Proprietary Technology Platform</h2>
    <p data-i18n="technology.sec_desc">The patented system that makes desert coffee cultivation viable.</p>
  </div>
  <div class="card" style="background:rgba(29,155,240,0.05);border-color:rgba(29,155,240,0.2);margin-bottom:32px">
    <div style="display:flex;align-items:center;gap:16px">
      <div style="font-size:40px">&#8471;</div>
      <div>
        <h3 style="color:var(--accent)" data-i18n="technology.patent_title">Patented Technology</h3>
        <p style="margin:0" data-i18n="technology.patent_info"></p>
        <p style="margin:4px 0 0" data-i18n="technology.patent_name"></p>
        <p style="margin:4px 0 0" data-i18n="technology.patent_applicant"></p>
        <p style="margin:4px 0 0" data-i18n="technology.patent_claims"></p>
      </div>
    </div>
  </div>
  <div class="card-grid col2">
    <div class="card">
      <h3 style="color:var(--green)" data-i18n="technology.s1_title">System 1 — AI Robotic Tissue Culture</h3>
      <p data-i18n="technology.s1_desc"></p>
      <ul style="color:var(--text-secondary);font-size:14px;line-height:1.8;margin-top:8px;padding-left:20px">
        <li data-i18n="technology.s1_li1"></li>
        <li data-i18n="technology.s1_li2"></li>
        <li data-i18n="technology.s1_li3"></li>
        <li data-i18n="technology.s1_li4"></li>
        <li data-i18n="technology.s1_li5"></li>
        <li data-i18n="technology.s1_li6"></li>
        <li data-i18n="technology.s1_li7"></li>
      </ul>
    </div>
    <div class="card">
      <h3 style="color:var(--accent)" data-i18n="technology.s2_title">System 2 — Gas-Liquid Atomization Hydroponics</h3>
      <p data-i18n="technology.s2_desc"></p>
      <ul style="color:var(--text-secondary);font-size:14px;line-height:1.8;margin-top:8px;padding-left:20px">
        <li data-i18n="technology.s2_li1"></li>
        <li data-i18n="technology.s2_li2"></li>
        <li data-i18n="technology.s2_li3"></li>
        <li data-i18n="technology.s2_li4"></li>
        <li data-i18n="technology.s2_li5"></li>
        <li data-i18n="technology.s2_li6"></li>
        <li data-i18n="technology.s2_li7"></li>
      </ul>
    </div>
  </div>
  <div class="card-grid col3" style="margin-top:24px">
    <div class="card" style="text-align:center"><div class="metric-large" style="color:var(--accent)" data-i18n="technology.metric1_val">15x</div><div class="metric-label" data-i18n="technology.metric1_lbl">Yield vs. Traditional Farm</div><p style="margin-top:8px" data-i18n="technology.metric1_desc"></p></div>
    <div class="card" style="text-align:center"><div class="metric-large" style="color:var(--green)" data-i18n="technology.metric2_val">12-14 mo</div><div class="metric-label" data-i18n="technology.metric2_lbl">First Harvest</div><p style="margin-top:8px" data-i18n="technology.metric2_desc"></p></div>
    <div class="card" style="text-align:center"><div class="metric-large" style="color:var(--orange)" data-i18n="technology.metric3_val">90%</div><div class="metric-label" data-i18n="technology.metric3_lbl">Water Reduction</div><p style="margin-top:8px" data-i18n="technology.metric3_desc"></p></div>
  </div>
</section>"""
    return HEAD.format(title="Technology Platform — PIF × NAPELL", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

def page_market():
    body = """<section class="section">
  <div class="section-header">
    <div class="num" data-i18n="market.sec_num">Section 04</div>
    <h2 data-i18n="market.sec_title">Market Opportunity &amp; Data</h2>
    <p data-i18n="market.sec_desc">Saudi coffee market metrics and the import substitution opportunity.</p>
  </div>
  <div class="card-grid col2">
    <div class="card">
      <h3 style="color:var(--accent)" data-i18n="market.t1_title">Saudi Coffee Market Size &amp; Growth</h3>
      <table>
        <tr><th>Metric</th><th>Value</th><th>Source</th></tr>
        <tr><td>Market Value (2024)</td><td style="color:var(--accent);font-weight:700">SAR 5-7 Billion</td><td>Al-Eqtisadiah</td></tr>
        <tr><td>Annual Growth Rate</td><td style="color:var(--green);font-weight:700">5%+</td><td>Maal Magazine</td></tr>
        <tr><td>Annual Consumption</td><td style="color:var(--accent);font-weight:700">80,000 tons</td><td>GAStat</td></tr>
        <tr><td>Daily Cups Consumed</td><td style="color:var(--accent);font-weight:700">36.5 Million</td><td>Al-Eqtisadiah</td></tr>
        <tr><td>Domestic Production (2023)</td><td style="color:var(--orange);font-weight:700">1,485 tons</td><td>Saudi Reef Program</td></tr>
        <tr><td>Production Target (2026)</td><td style="color:var(--green);font-weight:700">7,000 tons</td><td>MEWA</td></tr>
        <tr><td>Self-Sufficiency Rate</td><td style="color:var(--red);font-weight:700">~4% (target 2026)</td><td>Calculated</td></tr>
        <tr><td>Total Imports (2024)</td><td style="color:var(--accent);font-weight:700">188,000 tons</td><td>GAStat</td></tr>
      </table>
    </div>
    <div class="card">
      <h3 style="color:var(--green)" data-i18n="market.t2_title">Import Substitution Opportunity</h3>
      <table>
        <tr><th>Year</th><th>Import Volume</th><th>Napell Target</th><th>Substitution</th></tr>
        <tr><td>2024 (actual)</td><td>188,000 t</td><td>&mdash;</td><td>&mdash;</td></tr>
        <tr><td>Yr 3</td><td>~200,000 t</td><td>1,200 t</td><td style="color:var(--accent)">0.6%</td></tr>
        <tr><td>Yr 5</td><td>~210,000 t</td><td>4,800 t</td><td style="color:var(--accent)">2.3%</td></tr>
        <tr><td>Yr 7</td><td>~220,000 t</td><td>14,000 t</td><td style="color:var(--green)">6.4%</td></tr>
        <tr><td>Yr 10</td><td>~240,000 t</td><td>36,000 t</td><td style="color:var(--green)">15.0%</td></tr>
      </table>
      <p style="margin-top:16px;font-size:14px;color:var(--text-secondary)" data-i18n="market.t2_note"></p>
    </div>
  </div>
  <div class="chart-box"><h3 data-i18n="market.t1_chart_title">Saudi Arabia Coffee Market: Import Volume & Value Growth</h3><canvas id="importChart"></canvas></div>
  <div class="chart-box"><h3 data-i18n="market.t2_chart_title">Projected Import Substitution: Napell × PIF Scenario</h3><canvas id="substitutionChart"></canvas></div>
</section>"""
    return HEAD.format(title="Market Opportunity — PIF × NAPELL", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

def page_proposal():
    body = """<section class="section">
  <div class="section-header">
    <div class="num" data-i18n="proposal.sec_num">Section 05</div>
    <h2 data-i18n="proposal.sec_title">The Partnership Proposal</h2>
    <p data-i18n="proposal.sec_desc">A joint venture structure for sovereign coffee capability.</p>
  </div>
  <div class="card-grid col2">
    <div class="card" style="border-top:3px solid var(--accent)">
      <h3 style="color:var(--accent)" data-i18n="proposal.pif_title">PIF Contribution</h3>
      <ul style="color:var(--text-secondary);font-size:14px;line-height:2;padding-left:20px">
        <li data-i18n="proposal.pif_li1"></li>
        <li data-i18n="proposal.pif_li2"></li>
        <li data-i18n="proposal.pif_li3"></li>
        <li data-i18n="proposal.pif_li4"></li>
        <li data-i18n="proposal.pif_li5"></li>
        <li data-i18n="proposal.pif_li6"></li>
        <li data-i18n="proposal.pif_li7"></li>
      </ul>
    </div>
    <div class="card" style="border-top:3px solid var(--green)">
      <h3 style="color:var(--green)" data-i18n="proposal.napell_title">Napell Contribution</h3>
      <ul style="color:var(--text-secondary);font-size:14px;line-height:2;padding-left:20px">
        <li data-i18n="proposal.napell_li1"></li>
        <li data-i18n="proposal.napell_li2"></li>
        <li data-i18n="proposal.napell_li3"></li>
        <li data-i18n="proposal.napell_li4"></li>
        <li data-i18n="proposal.napell_li5"></li>
        <li data-i18n="proposal.napell_li6"></li>
        <li data-i18n="proposal.napell_li7"></li>
        <li data-i18n="proposal.napell_li8"></li>
        <li data-i18n="proposal.napell_li9"></li>
      </ul>
    </div>
  </div>
  <div class="card" style="margin-top:24px;text-align:center">
    <h3 style="color:var(--accent)" data-i18n="proposal.jv_title">Proposed JV Structure</h3>
    <div style="display:flex;align-items:center;justify-content:center;gap:32px;margin-top:24px;flex-wrap:wrap">
      <div style="background:var(--bg-card);border:1px solid var(--accent);border-radius:var(--radius);padding:24px 40px">
        <div style="font-size:36px;font-weight:900;color:var(--accent)">51%</div>
        <div style="font-size:13px;color:var(--text-muted);margin-top:4px" data-i18n="proposal.jv_pif_lbl">PIF / Saudi Entity</div>
      </div>
      <div style="font-size:24px;color:var(--text-muted)">+</div>
      <div style="background:var(--bg-card);border:1px solid var(--green);border-radius:var(--radius);padding:24px 40px">
        <div style="font-size:36px;font-weight:900;color:var(--green)">49%</div>
        <div style="font-size:13px;color:var(--text-muted);margin-top:4px" data-i18n="proposal.jv_napell_lbl">Napell Biotech</div>
      </div>
      <div style="font-size:24px;color:var(--text-muted)">=</div>
      <div style="background:linear-gradient(135deg,var(--accent-dim),rgba(34,197,94,0.1));border:1px solid var(--accent);border-radius:var(--radius);padding:24px 40px">
        <div style="font-size:20px;font-weight:700;color:var(--text-primary)" data-i18n="proposal.jv_entity">Saudi Coffee Technology Co.</div>
        <div style="font-size:12px;color:var(--accent);margin-top:4px" data-i18n="proposal.jv_entity_note">(proposed entity name)</div>
      </div>
    </div>
  </div>
</section>"""
    return HEAD.format(title="Partnership Proposal — PIF × NAPELL", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

def page_roadmap():
    body = """<section class="section">
  <div class="section-header">
    <div class="num" data-i18n="roadmap.sec_num">Section 06</div>
    <h2 data-i18n="roadmap.sec_title">Implementation Roadmap</h2>
    <p data-i18n="roadmap.sec_desc">Seven-year phased deployment with clear milestones.</p>
  </div>
  <div class="timeline">
    <div class="timeline-item">
      <div class="phase-label" data-i18n="roadmap.p1_label">Phase 1 — Year 1-2</div>
      <h3 style="color:var(--purple)" data-i18n="roadmap.p1_title">R&amp;D Center + Pilot Farm ($25-35M)</h3>
      <ul>
        <li data-i18n="roadmap.p1_li1"></li><li data-i18n="roadmap.p1_li2"></li><li data-i18n="roadmap.p1_li3"></li>
        <li data-i18n="roadmap.p1_li4"></li><li data-i18n="roadmap.p1_li5"></li><li data-i18n="roadmap.p1_li6"></li><li data-i18n="roadmap.p1_li7"></li>
      </ul>
    </div>
    <div class="timeline-item">
      <div class="phase-label" data-i18n="roadmap.p2_label">Phase 2 — Year 2-4</div>
      <h3 style="color:var(--accent)" data-i18n="roadmap.p2_title">Commercial-Scale Vertical Farm ($80-120M)</h3>
      <ul>
        <li data-i18n="roadmap.p2_li1"></li><li data-i18n="roadmap.p2_li2"></li><li data-i18n="roadmap.p2_li3"></li>
        <li data-i18n="roadmap.p2_li4"></li><li data-i18n="roadmap.p2_li5"></li><li data-i18n="roadmap.p2_li6"></li><li data-i18n="roadmap.p2_li7"></li><li data-i18n="roadmap.p2_li8"></li>
      </ul>
    </div>
    <div class="timeline-item">
      <div class="phase-label" data-i18n="roadmap.p3_label">Phase 3 — Year 5-7</div>
      <h3 style="color:var(--green)" data-i18n="roadmap.p3_title">National Scale &amp; GCC Export ($150-250M cumulative)</h3>
      <ul>
        <li data-i18n="roadmap.p3_li1"></li><li data-i18n="roadmap.p3_li2"></li><li data-i18n="roadmap.p3_li3"></li>
        <li data-i18n="roadmap.p3_li4"></li><li data-i18n="roadmap.p3_li5"></li><li data-i18n="roadmap.p3_li6"></li><li data-i18n="roadmap.p3_li7"></li><li data-i18n="roadmap.p3_li8"></li>
      </ul>
    </div>
    <div class="timeline-item">
      <div class="phase-label" data-i18n="roadmap.p4_label">Phase 4 — Year 8-10</div>
      <h3 style="color:var(--orange)" data-i18n="roadmap.p4_title">Global Brand &amp; Digital Twin Era</h3>
      <ul>
        <li data-i18n="roadmap.p4_li1"></li><li data-i18n="roadmap.p4_li2"></li><li data-i18n="roadmap.p4_li3"></li>
        <li data-i18n="roadmap.p4_li4"></li><li data-i18n="roadmap.p4_li5"></li><li data-i18n="roadmap.p4_li6"></li>
      </ul>
    </div>
  </div>
</section>"""
    return HEAD.format(title="Implementation Roadmap — PIF × NAPELL", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

def page_financials():
    body = """<section class="section">
  <div class="section-header">
    <div class="num" data-i18n="financials.sec_num">Section 07</div>
    <h2 data-i18n="financials.sec_title">Financial Projections</h2>
    <p data-i18n="financials.sec_desc">Unit economics, revenue streams, and return profile.</p>
  </div>
  <div class="card-grid col2">
    <div class="card">
      <h3 style="color:var(--accent)" data-i18n="financials.t1_title">Investment Allocation</h3>
      <table>
        <tr><th>Category</th><th>Phase 1</th><th>Phase 2</th><th>Phase 3</th><th>Total</th></tr>
        <tr><td>Facility Construction</td><td>$8M</td><td>$35M</td><td>$45M</td><td style="color:var(--accent)">$88M</td></tr>
        <tr><td>Robotic Equipment</td><td>$8M</td><td>$20M</td><td>$30M</td><td style="color:var(--accent)">$58M</td></tr>
        <tr><td>Atomization Systems</td><td>$3M</td><td>$18M</td><td>$25M</td><td style="color:var(--accent)">$46M</td></tr>
        <tr><td>Solar + Energy</td><td>$4M</td><td>$10M</td><td>$12M</td><td style="color:var(--accent)">$26M</td></tr>
        <tr><td>R&D + Training</td><td>$5M</td><td>$8M</td><td>$8M</td><td style="color:var(--accent)">$21M</td></tr>
        <tr><td>Processing Line</td><td>&mdash;</td><td>$8M</td><td>$10M</td><td style="color:var(--accent)">$18M</td></tr>
        <tr><td>Working Capital</td><td>$4M</td><td>$10M</td><td>$15M</td><td style="color:var(--accent)">$29M</td></tr>
        <tr style="font-weight:700"><td>Total</td><td>$32M</td><td>$109M</td><td>$145M</td><td style="color:var(--accent)">$286M</td></tr>
      </table>
    </div>
    <div class="card">
      <h3 style="color:var(--green)" data-i18n="financials.t2_title">Projected P&amp;L Summary (Year 5)</h3>
      <table>
        <tr><th>Line Item</th><th>Amount</th></tr>
        <tr><td>Green Bean Revenue</td><td style="color:var(--accent)">$38-62M</td></tr>
        <tr><td>Roasted Coffee (B2B)</td><td style="color:var(--accent)">$25-40M</td></tr>
        <tr><td>Retail &amp; DTC</td><td style="color:var(--accent)">$15-25M</td></tr>
        <tr><td>Tourism &amp; IP Licensing</td><td style="color:var(--accent)">$8-12M</td></tr>
        <tr style="font-weight:700"><td>Total Revenue</td><td style="color:var(--green)">$86-139M</td></tr>
        <tr><td>COGS</td><td style="color:var(--red)">($35-55M)</td></tr>
        <tr style="font-weight:700"><td>Gross Profit</td><td style="color:var(--green)">$51-84M</td></tr>
        <tr style="font-weight:700"><td>Gross Margin</td><td style="color:var(--green)">59-60%</td></tr>
        <tr><td>Operating Expenses</td><td style="color:var(--red)">($20-25M)</td></tr>
        <tr style="font-weight:700"><td>EBITDA</td><td style="color:var(--green)">$31-59M</td></tr>
        <tr style="font-weight:700"><td>EBITDA Margin</td><td style="color:var(--green)">35-42%</td></tr>
      </table>
    </div>
  </div>
  <div class="data-row" style="margin-top:24px">
    <div class="data-item"><div class="value" style="color:var(--accent)" data-i18n="financials.m1_val">5-7 yr</div><div class="label" data-i18n="financials.m1_lbl">Payback Period</div></div>
    <div class="data-item"><div class="value" style="color:var(--green)" data-i18n="financials.m2_val">18-24%</div><div class="label" data-i18n="financials.m2_lbl">Project IRR</div></div>
    <div class="data-item"><div class="value" style="color:var(--orange)" data-i18n="financials.m3_val">3.5-4.5x</div><div class="label" data-i18n="financials.m3_lbl">MOIC (10-year)</div></div>
    <div class="data-item"><div class="value" style="color:var(--purple)" data-i18n="financials.m4_val">350+</div><div class="label" data-i18n="financials.m4_lbl">Jobs Created (high-skilled)</div></div>
  </div>
  <div class="chart-box"><h3 data-i18n="financials.chart_title">10-Year Revenue & EBITDA Projection</h3><canvas id="projectionChart"></canvas></div>
</section>"""
    return HEAD.format(title="Financial Projections — PIF × NAPELL", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

def page_risks():
    body = """<section class="section">
  <div class="section-header">
    <div class="num" data-i18n="risks.sec_num">Section 08</div>
    <h2 data-i18n="risks.sec_title">Risk Analysis &amp; Mitigation</h2>
    <p data-i18n="risks.sec_desc">Key risks identified with mitigation strategies.</p>
  </div>
  <table>
    <tr><th style="width:20%">Risk</th><th style="width:15%">Severity</th><th style="width:30%">Description</th><th style="width:35%">Mitigation</th></tr>
    <tr><td><strong data-i18n="risks.r1_name">Energy Cost</strong></td><td><span class="tag orange" data-i18n="risks.r1_sev">Medium</span></td><td data-i18n="risks.r1_desc"></td><td data-i18n="risks.r1_mit"></td></tr>
    <tr><td><strong data-i18n="risks.r2_name">Technology Transfer</strong></td><td><span class="tag orange" data-i18n="risks.r2_sev">Medium</span></td><td data-i18n="risks.r2_desc"></td><td data-i18n="risks.r2_mit"></td></tr>
    <tr><td><strong data-i18n="risks.r3_name">Long-term Reliability</strong></td><td><span class="tag orange" data-i18n="risks.r3_sev">Medium</span></td><td data-i18n="risks.r3_desc"></td><td data-i18n="risks.r3_mit"></td></tr>
    <tr><td><strong data-i18n="risks.r4_name">Market Acceptance</strong></td><td><span class="tag green" data-i18n="risks.r4_sev">Low</span></td><td data-i18n="risks.r4_desc"></td><td data-i18n="risks.r4_mit"></td></tr>
    <tr><td><strong data-i18n="risks.r5_name">Regulatory</strong></td><td><span class="tag green" data-i18n="risks.r5_sev">Low</span></td><td data-i18n="risks.r5_desc"></td><td data-i18n="risks.r5_mit"></td></tr>
    <tr><td><strong data-i18n="risks.r6_name">Water Supply</strong></td><td><span class="tag green" data-i18n="risks.r6_sev">Low</span></td><td data-i18n="risks.r6_desc"></td><td data-i18n="risks.r6_mit"></td></tr>
  </table>
</section>"""
    return HEAD.format(title="Risk Analysis — PIF × NAPELL", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

def page_alignment():
    body = """<section class="section">
  <div class="section-header">
    <div class="num" data-i18n="alignment.sec_num">Section 09</div>
    <h2 data-i18n="alignment.sec_title">Strategic Alignment: PIF &amp; Vision 2030</h2>
    <p data-i18n="alignment.sec_desc">How this partnership fits within PIF's existing portfolio and national strategy.</p>
  </div>
  <div class="card-grid col3">
    <div class="card"><h3 style="color:var(--accent)" data-i18n="alignment.c1_title">Food Security</h3><p data-i18n="alignment.c1_text"></p></div>
    <div class="card"><h3 style="color:var(--green)" data-i18n="alignment.c2_title">Economic Diversification</h3><p data-i18n="alignment.c2_text"></p></div>
    <div class="card"><h3 style="color:var(--purple)" data-i18n="alignment.c3_title">Technology Transfer</h3><p data-i18n="alignment.c3_text"></p></div>
    <div class="card"><h3 style="color:var(--orange)" data-i18n="alignment.c4_title">PIF Portfolio Synergy</h3><p data-i18n="alignment.c4_text"></p></div>
    <div class="card"><h3 style="color:var(--red)" data-i18n="alignment.c5_title">Tourism &amp; Brand</h3><p data-i18n="alignment.c5_text"></p></div>
    <div class="card"><h3 style="color:var(--accent)" data-i18n="alignment.c6_title">Environmental Leadership</h3><p data-i18n="alignment.c6_text"></p></div>
  </div>
</section>"""
    return HEAD.format(title="Strategic Alignment — PIF × NAPELL", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

def page_blueprints():
    body = """<section class="section">
  <div class="section-header">
    <div class="num" data-i18n="blueprints.sec_num">Section 10</div>
    <h2 data-i18n="blueprints.sec_title">Technical Industrial Blueprints</h2>
    <p data-i18n="blueprints.sec_desc">Detailed engineering drawings for the A3 robotic arm tissue culture system and gas-liquid atomization cultivation principle.</p>
  </div>
  <div class="bp-tabs">
    <button class="bp-tab active" onclick="switchBPTab('robotic')" data-i18n="blueprints.tab1">A3 Robotic Arm + AI Vision System</button>
    <button class="bp-tab" onclick="switchBPTab('aeroponic')" data-i18n="blueprints.tab2">Gas-Liquid Atomization Cultivation</button>
  </div>
  <div id="bp-robotic" class="bp-panel active">
    <div class="card" style="margin-bottom:16px">
      <h3 style="color:var(--accent)" data-i18n="blueprints.bp1_title"></h3>
      <p style="color:var(--text-secondary);font-size:14px;line-height:1.7;margin-top:8px" data-i18n="blueprints.bp1_desc"></p>
    </div>
    <div class="blueprint-container">
      <img src="assets/blueprint-robotic-arm.svg" alt="A3 Robotic Arm Blueprint" style="width:100%;height:auto;border-radius:var(--radius);border:1px solid var(--border-color)">
    </div>
    <p style="font-size:12px;color:var(--text-muted);margin-top:8px;text-align:center" data-i18n="blueprints.bp1_caption"></p>
    <div class="data-row" style="margin-top:16px">
      <div class="data-item"><div class="value" style="color:var(--accent)">&plusmn;0.02mm</div><div class="label" data-i18n="blueprints.bp1_m1_lbl">Repeatability</div></div>
      <div class="data-item"><div class="value" style="color:var(--green)">22 sec</div><div class="label" data-i18n="blueprints.bp1_m2_lbl">Per Seedling Cycle</div></div>
      <div class="data-item"><div class="value" style="color:var(--orange)">100K+</div><div class="label" data-i18n="blueprints.bp1_m3_lbl">RL Training Epochs</div></div>
    </div>
  </div>
  <div id="bp-aeroponic" class="bp-panel">
    <div class="card" style="margin-bottom:16px">
      <h3 style="color:var(--green)" data-i18n="blueprints.bp2_title"></h3>
      <p style="color:var(--text-secondary);font-size:14px;line-height:1.7;margin-top:8px" data-i18n="blueprints.bp2_desc"></p>
    </div>
    <div class="blueprint-container">
      <img src="assets/blueprint-aeroponic.svg" alt="Aeroponic System Blueprint" style="width:100%;height:auto;border-radius:var(--radius);border:1px solid var(--border-color)">
    </div>
    <p style="font-size:12px;color:var(--text-muted);margin-top:8px;text-align:center" data-i18n="blueprints.bp2_caption"></p>
    <div class="data-row" style="margin-top:16px">
      <div class="data-item"><div class="value" style="color:var(--accent)">2,100 L/kg</div><div class="label" data-i18n="blueprints.bp2_m1_lbl">L/kg Water (vs 21,000 traditional)</div></div>
      <div class="data-item"><div class="value" style="color:var(--green)">5-30 &micro;m</div><div class="label" data-i18n="blueprints.bp2_m2_lbl">Droplet Size Range</div></div>
      <div class="data-item"><div class="value" style="color:var(--orange)">300%</div><div class="label" data-i18n="blueprints.bp2_m3_lbl">Root Oxygenation vs DWC</div></div>
    </div>
  </div>
</section>"""
    return HEAD.format(title="Technical Blueprints — PIF × NAPELL", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

def page_drawings():
    body = """<section class="section">
  <div class="section-header">
    <div class="num" data-i18n="drawings.sec_num">Section 11</div>
    <h2 data-i18n="drawings.sec_title">Technical Engineering Drawings</h2>
    <p data-i18n="drawings.sec_desc">Complete system architecture, facility layout, value chain, and financial diagrams.</p>
  </div>
  <div class="blueprint-container">
    <img src="assets/tech-drawings.svg" alt="Technical Engineering Drawings" style="width:100%;height:auto;border-radius:var(--radius);border:1px solid var(--border-color)">
  </div>
  <p style="font-size:12px;color:var(--text-muted);margin-top:8px;text-align:center" data-i18n="drawings.caption"></p>
  <div class="card" style="margin-top:24px">
    <h3 style="color:var(--accent)" data-i18n="drawings.notes_title">Technical Drawing Notes</h3>
    <p style="color:var(--text-secondary);font-size:14px;line-height:1.8;margin-top:8px" data-i18n="drawings.notes_text"></p>
  </div>
</section>"""
    return HEAD.format(title="Engineering Drawings — PIF × NAPELL", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

def page_contact():
    body = """<section class="section">
  <div class="section-header">
    <div class="num" data-i18n="contact.sec_num">Next Steps</div>
    <h2 data-i18n="contact.sec_title">Let's Build Saudi Arabia's Coffee Future</h2>
    <p data-i18n="contact.sec_desc">We are ready to present this proposal in person and begin the due diligence process.</p>
  </div>
  <div class="card-grid col3" style="margin-bottom:32px">
    <div class="card" style="border-top:3px solid var(--purple)">
      <div class="step-num" data-i18n="contact.s1_title">Step 1</div>
      <h3 style="color:var(--purple)" data-i18n="contact.s1_name">Initial Meeting</h3>
      <p style="color:var(--text-secondary);font-size:14px;line-height:1.7" data-i18n="contact.s1_desc"></p>
    </div>
    <div class="card" style="border-top:3px solid var(--accent)">
      <div class="step-num" data-i18n="contact.s2_title">Step 2</div>
      <h3 style="color:var(--accent)" data-i18n="contact.s2_name">Technical Due Diligence</h3>
      <p style="color:var(--text-secondary);font-size:14px;line-height:1.7" data-i18n="contact.s2_desc"></p>
    </div>
    <div class="card" style="border-top:3px solid var(--green)">
      <div class="step-num" data-i18n="contact.s3_title">Step 3</div>
      <h3 style="color:var(--green)" data-i18n="contact.s3_name">Term Sheet</h3>
      <p style="color:var(--text-secondary);font-size:14px;line-height:1.7" data-i18n="contact.s3_desc"></p>
    </div>
  </div>
  <div class="card" style="background:linear-gradient(135deg,rgba(29,155,240,0.08),rgba(34,197,94,0.08));border:1px solid var(--accent)">
    <h3 style="color:var(--accent)" data-i18n="contact.contact_title">Contact Napell Biotech</h3>
    <div class="contact-grid">
      <div class="contact-item">
        <div class="contact-icon" style="color:var(--green)">&#9993;</div>
        <div>
          <div class="contact-label">Email</div>
          <a href="mailto:erik.wong@napell.bio" style="color:var(--accent);text-decoration:none">erik.wong@napell.bio</a>
        </div>
      </div>
      <div class="contact-item">
        <div class="contact-icon" style="color:var(--accent)">&#9742;</div>
        <div>
          <div class="contact-label">WhatsApp</div>
          <a href="https://wa.me/85293188252" style="color:var(--accent);text-decoration:none">+852 9318 8252</a>
        </div>
      </div>
      <div class="contact-item">
        <div class="contact-icon" style="color:var(--purple)">&#9742;</div>
        <div>
          <div class="contact-label">WeChat</div>
          <span style="color:var(--text-primary)">+86 158 0022 2338</span>
        </div>
      </div>
    </div>
    <p style="margin-top:24px;font-size:13px;color:var(--text-muted);text-align:center" data-i18n="contact.contact_ref"></p>
  </div>
</section>"""
    return HEAD.format(title="Connect — PIF × NAPELL", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

def page_video():
    body = """<section class="section">
  <div class="section-header">
    <div class="num" data-i18n="video.sec_num">Section 12</div>
    <h2 data-i18n="video.sec_title">Video Brief — El Niño 2026 &amp; the Aeroponic Answer</h2>
    <p data-i18n="video.sec_desc">A 68-second climate intelligence briefing produced by Napell BIO — connecting the global El Niño 2026 crisis to the aeroponic solution and the Saudi opportunity.</p>
  </div>

  <!-- Video Player -->
  <div style="max-width:960px;margin:0 auto 40px;background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden">
    <video controls playsinline preload="metadata" style="width:100%;display:block;background:#000" poster="assets/coffee-aeroponic-napellbio.mp4">
      <source src="assets/coffee-aeroponic-napellbio.mp4" type="video/mp4">
      <p data-i18n="video.no_video_warning">Your browser does not support embedded video. Download it instead:</p>
    </video>
    <div style="padding:16px 24px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px">
      <div>
        <div style="font-weight:700;font-size:15px;color:var(--text-primary)" data-i18n="video.video_label">Watch Briefing</div>
        <div style="font-size:12px;color:var(--text-muted);margin-top:2px" data-i18n="video.video_sublabel">68 seconds · 1080p · Mandarin narration with on-screen text in EN/中文/العربية</div>
      </div>
      <a href="assets/coffee-aeroponic-napellbio.mp4" download class="nav-cta" style="font-size:13px" data-i18n="video.download_btn">Download MP4 (8.2 MB)</a>
    </div>
  </div>

  <!-- Analysis -->
  <div style="max-width:960px;margin:0 auto">
    <h3 style="font-size:24px;margin-bottom:12px" data-i18n="video.analysis_title">Why This Video Matters to the Saudi Coffee Chain</h3>
    <p style="font-size:15px;color:var(--text-secondary);margin-bottom:40px;line-height:1.8" data-i18n="video.analysis_intro">This briefing distills the strategic case in 68 seconds. It is a market-reality video — not a product demo — designed to anchor the conversation between Napell and PIF in three layers of evidence:</p>

    <!-- Layer 1 -->
    <div class="card" style="margin-bottom:24px;border-left:3px solid var(--accent)">
      <h4 style="font-size:17px;margin-bottom:12px;color:var(--accent)" data-i18n="video.layer1_title">Layer 1 — The Threat is Real, Quantified, and Accelerating</h4>
      <p style="font-size:14px;color:var(--text-secondary);line-height:1.9" data-i18n="video.layer1_text">Using data sourced from the International Coffee Organization (ICO), World Coffee Research, and NOAA's 2026 climate forecast, the video quantifies the 2026 El Niño impact: +2.8°C mean temperature increase, –38% rainfall deficit, and 24% loss of coffee planting area. Global production is projected to fall 37% (from 98M bags in 2022 to 62M in 2026P), while Arabica futures prices are projected to surge 293% (from $1.22/lb in 2020 to $4.80 in 2026P). Four flagship origins — Brazil, Colombia, Vietnam, Ethiopia — are shown to be at severe-to-extreme risk. The video further cites ICO's projection that <strong>50% of global coffee arable land will disappear by 2050</strong>, directly threatening 120 million livelihoods.</p>
    </div>

    <!-- Layer 2 -->
    <div class="card" style="margin-bottom:24px;border-left:3px solid var(--purple)">
      <h4 style="font-size:17px;margin-bottom:12px;color:var(--purple)" data-i18n="video.layer2_title">Layer 2 — Traditional Soil Cultivation Cannot Survive This</h4>
      <p style="font-size:14px;color:var(--text-secondary);line-height:1.9" data-i18n="video.layer2_text">The video identifies three systemic vulnerabilities that traditional soil farming cannot mitigate: (1) <strong>Climate fragility</strong> — coffee requires 1,500–2,000mm stable rainfall and 18–24°C temperatures; El Niño breaks both, triggering a 65% surge in crop pests/diseases. (2) <strong>Water waste &amp; soil degradation</strong> — soil-grown coffee consumes up to 140 liters of water per cup and loses 35% of topsoil per decade. (3) <strong>Pest outbreak pressure</strong> — coffee leaf rust and coffee berry borer spread 55% faster under El Niño conditions, with soil farms having no isolation barrier, causing up to 50% yield losses and $340/ha extra pesticide cost.</p>
    </div>

    <!-- Layer 3 -->
    <div class="card" style="margin-bottom:40px;border-left:3px solid var(--accent)">
      <h4 style="font-size:17px;margin-bottom:12px;color:var(--accent)" data-i18n="video.layer3_title">Layer 3 — Aeroponics is the Only Defensible Answer</h4>
      <p style="font-size:14px;color:var(--text-secondary);line-height:1.9" data-i18n="video.layer3_text">The video closes with Napell BIO's aeroponic system delivering three structural wins: <strong>95% water reduction</strong> vs soil (root misting has no runoff), <strong>365-day uninterrupted production</strong> in fully climate-controlled 20–22°C vertical towers with 1,600 lux lighting, and <strong>3× growth speed</strong> via oxygen-rich nutrient mist that accelerates mineral uptake. The harvest cycle drops from 4 years to 12–14 months. This is precisely why Saudi Arabia — with its 2.4B m³ renewable water ceiling and Vision 2030 food-security mandate — is the highest-leverage geography in the world for this technology.</p>
    </div>

    <!-- Investment Implications -->
    <h3 style="font-size:22px;margin-bottom:20px" data-i18n="video.inv_title">Implications for the Saudi Arabia Investment Thesis</h3>
    <div class="card-grid col3" style="margin-bottom:40px">
      <div class="card"><p style="font-size:14px;color:var(--text-secondary);line-height:1.9" data-i18n="video.inv1">Time compression — Saudi cannot wait 25 years for traditional farms to be retrofitted. The El Niño crisis is <strong>now</strong>. Aeroponics is the only path to sovereign coffee security in this decade.</p></div>
      <div class="card"><p style="font-size:14px;color:var(--text-secondary);line-height:1.9" data-i18n="video.inv2">Price tailwind — at projected $4.80/lb Arabica and tightening supply, every ton Napell produces in Saudi is sold into a structural bull market, accelerating the JV's path to breakeven.</p></div>
      <div class="card"><p style="font-size:14px;color:var(--text-secondary);line-height:1.9" data-i18n="video.inv3">Strategic optionality — PIF's investment de-risks Vision 2030's food-security pillar while capturing a defensible position in the global indoor-coffee technology stack that no other Gulf sovereign is positioned to take.</p></div>
    </div>

    <!-- Transcript -->
    <h3 style="font-size:22px;margin-bottom:20px" data-i18n="video.transcript_title">On-screen Text &amp; Data (Key Frames)</h3>
    <div style="display:flex;flex-direction:column;gap:16px;margin-bottom:40px">
      <div class="card" style="padding:16px 20px"><span style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">0–5s</span><p style="font-size:14px;color:var(--text-secondary);margin-top:6px;line-height:1.7" data-i18n="video.transcript_t0_5">Opening — Napell BIO logo + tagline: <em>"Growing the future, today"</em></p></div>
      <div class="card" style="padding:16px 20px"><span style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">~10s</span><p style="font-size:14px;color:var(--text-secondary);margin-top:6px;line-height:1.7" data-i18n="video.transcript_t10">Title — <em>"EL NIÑO 2026 → COFFEE CRISIS"</em>. Subtitle in English: <em>"How the world's most extreme El Niño threatens global coffee supply, and the aeroponic technology changing everything"</em>.</p></div>
      <div class="card" style="padding:16px 20px"><span style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">~15s</span><p style="font-size:14px;color:var(--text-secondary);margin-top:6px;line-height:1.7" data-i18n="video.transcript_t15">Section — <em>"Top coffee origins face severe threats"</em>: Brazil 88% risk, Colombia 74%, Vietnam 92%, Ethiopia 68%. Headline stats: +2.8°C, –38% rainfall, 24% planting area lost.</p></div>
      <div class="card" style="padding:16px 20px"><span style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">~25s</span><p style="font-size:14px;color:var(--text-secondary);margin-top:6px;line-height:1.7" data-i18n="video.transcript_t25">Section — <em>"Supply shock &amp; price surge"</em>: Global production –37% (98M → 62M bags, 2022 → 2026P); Arabica futures +293% ($1.22 → $4.80/lb, 2020 → 2026P). Source: ICO + WCR + NOAA.</p></div>
      <div class="card" style="padding:16px 20px"><span style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">~35s</span><p style="font-size:14px;color:var(--text-secondary);margin-top:6px;line-height:1.7" data-i18n="video.transcript_t35">Section — <em>"Coffee arable land will shrink 50% by 2050"</em>. Source: ICO.</p></div>
      <div class="card" style="padding:16px 20px"><span style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">~40s</span><p style="font-size:14px;color:var(--text-secondary);margin-top:6px;line-height:1.7" data-i18n="video.transcript_t40">Section — <em>"3 systemic vulnerabilities"</em>: ① Climate fragility (1,500–2,000mm rain &amp; 18–24°C required; +65% pest surge). ② Water waste &amp; soil degradation (140L water per cup; 35% topsoil loss/decade). ③ Pest outbreak pressure (+55% leaf rust; +$340/ha pesticide cost; up to 50% yield loss).</p></div>
      <div class="card" style="padding:16px 20px"><span style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">~55s</span><p style="font-size:14px;color:var(--text-secondary);margin-top:6px;line-height:1.7" data-i18n="video.transcript_t55">Section — <em>"Aeroponic Coffee Cultivation System"</em>: 95% water saving, 365-day uninterrupted production, 3× growth speed, harvest cycle 4 yr → 12–14 mo.</p></div>
      <div class="card" style="padding:16px 20px"><span style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">~65s</span><p style="font-size:14px;color:var(--text-secondary);margin-top:6px;line-height:1.7" data-i18n="video.transcript_t65">Closing — Napell BIO + <em>"Growing the future, today"</em>. Two closing messages: (1) 2026 Super El Niño is disrupting the global coffee supply chain. (2) Traditional soil cultivation cannot withstand extreme climate shocks.</p></div>
    </div>

    <!-- How to Use This Video -->
    <h3 style="font-size:22px;margin-bottom:20px" data-i18n="video.use_title">How to Use This Video with PIF</h3>
    <div style="display:flex;flex-direction:column;gap:16px;margin-bottom:20px">
      <div class="card" style="padding:16px 20px;display:flex;align-items:flex-start;gap:14px">
        <span style="font-size:18px;flex-shrink:0;margin-top:2px">1.</span>
        <p style="font-size:14px;color:var(--text-secondary);line-height:1.7;margin:0" data-i18n="video.use1"><strong>Open the meeting</strong> with the 68-second briefing — it sets the urgency frame in under two minutes and reaches the C-suite without a slide deck.</p>
      </div>
      <div class="card" style="padding:16px 20px;display:flex;align-items:flex-start;gap:14px">
        <span style="font-size:18px;flex-shrink:0;margin-top:2px">2.</span>
        <p style="font-size:14px;color:var(--text-secondary);line-height:1.7;margin:0" data-i18n="video.use2"><strong>Anchor the data</strong> by linking to the source citations (ICO, NOAA, WCR) shown in the closing frames — PIF analysts can verify independently.</p>
      </div>
      <div class="card" style="padding:16px 20px;display:flex;align-items:flex-start;gap:14px">
        <span style="font-size:18px;flex-shrink:0;margin-top:2px">3.</span>
        <p style="font-size:14px;color:var(--text-secondary);line-height:1.7;margin:0" data-i18n="video.use3"><strong>Hand off</strong> to Section 04 (Market) and Section 02 (Context) of this proposal for the full financial and strategic depth — the video is the hook, the proposal is the close.</p>
      </div>
    </div>
  </div>
</section>"""
    return HEAD.format(title="Video Brief — PIF × NAPELL", nav=NAV_HTML) + '<div class="page-wrapper">' + body + '</div>' + TAIL.format(footer=FOOTER_HTML)

# ============================================================
# Main Execution
# ============================================================
if __name__ == "__main__":
    os.makedirs(os.path.join(BASE, "js"), exist_ok=True)

    # Generate i18n.js
    with open(os.path.join(BASE, "js", "i18n.js"), "w", encoding="utf-8") as f:
        f.write(gen_i18n_js())
    print("Generated js/i18n.js")

    # Generate all pages
    pages = {
        "index.html": page_index(),
        "context.html": page_context(),
        "technology.html": page_technology(),
        "market.html": page_market(),
        "proposal.html": page_proposal(),
        "roadmap.html": page_roadmap(),
        "financials.html": page_financials(),
        "risks.html": page_risks(),
        "alignment.html": page_alignment(),
        "blueprints.html": page_blueprints(),
        "drawings.html": page_drawings(),
        "video.html": page_video(),
        "contact.html": page_contact(),
    }
    for name, html in pages.items():
        with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {name}")

    print(f"\nDone! {len(pages)} pages generated.")