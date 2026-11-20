# -*- coding: utf-8 -*-
import json
import os

scratch_dir = r"C:\Users\abdou1\.gemini\antigravity\scratch\bighouse-menu"
json_path = os.path.join(scratch_dir, "categories_data.json")
output_path = os.path.join(scratch_dir, "index.html")

with open(json_path, "r", encoding="utf-8") as f:
    categories = json.load(f)

# Serialize categories to JSON for client-side embedding
categories_json = json.dumps(categories, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="fr" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>Big House Restaurant & Pizzeria | Menu Digital | Rouiba مطعم بيغ هاوس رويبة</title>
    
    <!-- Meta & Open Graph Tags -->
    <meta name="description" content="Menu digital officiel de Big House Restaurant & Pizzeria à Rouiba, Alger. Grillades, pizzas au feu de bois, viandes, pâtes, poissons, cocktails et desserts. قائمة طعام مطعم بيغ هاوس رويبة.">
    <meta name="theme-color" content="#0d0e11">
    <meta property="og:title" content="Big House Restaurant & Pizzeria — Menu Digital">
    <meta property="og:description" content="« Chez nous on mange bien, On s'en souvient, Et on revient. » — 16 Lot Communal, Rouiba, Alger">
    <meta property="og:type" content="restaurant.menu">
    <meta property="og:image" content="https://abouda10ranem-source.github.io/bighouse-menu/images/logo.png">
    <meta property="og:url" content="https://abouda10ranem-source.github.io/bighouse-menu/">

    <!-- Google Fonts: Poppins (Latin) & Tajawal / Cairo (Arabic) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600;1,700&family=Poppins:wght@300;400;500;600;700&family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">

    <style>
        :root {{
            --bg-body: #0a0b0e;
            --bg-container: #101216;
            --bg-card: rgba(22, 25, 33, 0.88);
            --bg-card-hover: rgba(30, 34, 45, 0.95);
            --bg-sticky: rgba(14, 16, 21, 0.92);
            --bg-pill: rgba(255, 255, 255, 0.06);
            --bg-pill-hover: rgba(255, 255, 255, 0.12);
            --bg-pill-active: #d32f2f;
            
            --accent-red: #d32f2f;
            --accent-red-hover: #e53935;
            --accent-red-glow: rgba(211, 47, 47, 0.4);
            --accent-red-subtle: rgba(211, 47, 47, 0.14);
            --accent-gold: #f59e0b;
            --accent-gold-subtle: rgba(245, 158, 11, 0.12);
            --green-online: #22c55e;

            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            
            --border-subtle: rgba(255, 255, 255, 0.08);
            --border-card: rgba(255, 255, 255, 0.06);
            --border-red: rgba(211, 47, 47, 0.45);
            
            --radius-xs: 6px;
            --radius-sm: 10px;
            --radius-md: 14px;
            --radius-lg: 20px;
            --radius-pill: 9999px;

            --shadow-sm: 0 4px 12px rgba(0, 0, 0, 0.3);
            --shadow-card: 0 6px 20px rgba(0, 0, 0, 0.4);
            --shadow-glow: 0 0 25px var(--accent-red-glow);

            --font-body: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            --font-title: 'Playfair Display', Georgia, serif;
            --font-arabic: 'Tajawal', 'Cairo', 'Poppins', sans-serif;
        }}

        /* Reset & Base */
        *, *::before, *::after {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }}

        html {{
            scroll-behavior: smooth;
            font-size: 15px;
            background-color: var(--bg-body);
        }}

        body {{
            font-family: var(--font-body);
            background-color: var(--bg-body);
            color: var(--text-primary);
            min-height: 100vh;
            line-height: 1.5;
            display: flex;
            justify-content: center;
            overflow-x: hidden;
        }}

        /* Arabic Typography & RTL */
        html[dir="rtl"] body {{
            font-family: var(--font-arabic);
            direction: rtl;
            text-align: right;
        }}
        html[dir="rtl"] .brand-name {{
            font-family: var(--font-arabic);
            font-weight: 900;
            letter-spacing: 0;
        }}
        html[dir="rtl"] .brand-slogan {{
            font-family: var(--font-arabic);
            font-style: normal;
            font-weight: 600;
        }}
        html[dir="rtl"] .category-title {{
            font-family: var(--font-arabic);
            letter-spacing: 0;
        }}
        html[dir="rtl"] .dish-title {{
            font-family: var(--font-arabic);
            font-weight: 700;
        }}

        /* Mobile Container (NordQR format max-width: 500px) */
        .app-container {{
            width: 100%;
            max-width: 520px;
            background-color: var(--bg-container);
            min-height: 100vh;
            position: relative;
            box-shadow: 0 0 60px rgba(0, 0, 0, 0.9);
            border-left: 1px solid var(--border-subtle);
            border-right: 1px solid var(--border-subtle);
            padding-bottom: 50px;
        }}

        /* Top Bar: Language Switcher & QR Shortcut */
        .top-navbar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 18px;
            background: rgba(14, 16, 21, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-subtle);
            position: sticky;
            top: 0;
            z-index: 100;
        }}

        .brand-mini {{
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            color: var(--text-primary);
        }}
        .brand-mini img {{
            height: 32px;
            width: auto;
            border-radius: 6px;
        }}
        .brand-mini-text {{
            font-weight: 700;
            font-size: 1.05rem;
            letter-spacing: 0.5px;
        }}
        .brand-mini-text span {{
            color: var(--accent-red);
        }}

        /* Language Toggle Switcher */
        .lang-switch {{
            display: flex;
            align-items: center;
            background: rgba(255, 255, 255, 0.08);
            border-radius: var(--radius-pill);
            padding: 3px;
            border: 1px solid var(--border-subtle);
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);
        }}
        .lang-btn {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            font-size: 0.76rem;
            font-weight: 600;
            padding: 5px 12px;
            border-radius: var(--radius-pill);
            cursor: pointer;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            align-items: center;
            gap: 4px;
        }}
        .lang-btn.active {{
            background: var(--accent-red);
            color: #ffffff;
            box-shadow: 0 2px 8px var(--accent-red-glow);
        }}

        /* Hero Header with Restaurant Ambiance Cover */
        .hero-banner {{
            position: relative;
            height: 180px;
            overflow: hidden;
            background: #111;
        }}
        .hero-banner img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: brightness(0.65);
            transform: scale(1.02);
            transition: transform 0.5s ease;
        }}
        .hero-banner-overlay {{
            position: absolute;
            inset: 0;
            background: linear-gradient(to bottom, rgba(16, 18, 22, 0.2), rgba(16, 18, 22, 1));
        }}

        .hero-content {{
            padding: 0 20px 24px;
            text-align: center;
            margin-top: -55px;
            position: relative;
            z-index: 2;
        }}

        .logo-emblem {{
            width: 95px;
            height: 95px;
            margin: 0 auto 14px;
            border-radius: 50%;
            background: #16181f;
            border: 2px solid var(--accent-red);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.7), 0 0 20px var(--accent-red-glow);
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s ease;
        }}
        .logo-emblem:hover {{
            transform: scale(1.05);
        }}
        .logo-emblem img {{
            width: 82%;
            height: 82%;
            object-fit: contain;
        }}

        .status-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(34, 197, 94, 0.12);
            border: 1px solid rgba(34, 197, 94, 0.3);
            color: var(--green-online);
            padding: 4px 12px;
            border-radius: var(--radius-pill);
            font-size: 0.72rem;
            font-weight: 600;
            margin-bottom: 10px;
            letter-spacing: 0.5px;
        }}
        .status-dot {{
            width: 7px;
            height: 7px;
            background-color: var(--green-online);
            border-radius: 50%;
            box-shadow: 0 0 8px var(--green-online);
            animation: pulseDot 2s infinite ease-in-out;
        }}
        @keyframes pulseDot {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.4; transform: scale(0.85); }}
        }}

        .brand-name {{
            font-family: var(--font-title);
            font-size: 2.1rem;
            font-weight: 800;
            letter-spacing: 1.5px;
            color: var(--text-primary);
            text-transform: uppercase;
            margin-bottom: 3px;
            line-height: 1.15;
        }}
        .brand-name span {{
            color: var(--accent-red);
        }}

        .brand-subtitle {{
            font-size: 0.85rem;
            letter-spacing: 2px;
            color: var(--accent-gold);
            font-weight: 600;
            margin-bottom: 12px;
        }}

        .brand-slogan {{
            font-family: var(--font-title);
            font-style: italic;
            font-size: 0.95rem;
            color: #e2e8f0;
            line-height: 1.45;
            max-width: 380px;
            margin: 0 auto 18px;
            padding: 8px 16px;
            background: rgba(255, 255, 255, 0.03);
            border-radius: var(--radius-sm);
            border-left: 3px solid var(--accent-red);
            border-right: 3px solid var(--accent-red);
        }}

        /* Info Chips */
        .info-grid {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 8px;
            margin-bottom: 16px;
        }}
        .info-chip {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-pill);
            padding: 6px 12px;
            font-size: 0.74rem;
            color: var(--text-secondary);
            text-decoration: none;
            transition: all 0.2s ease;
        }}
        .info-chip:hover {{
            background: rgba(255, 255, 255, 0.09);
            color: var(--text-primary);
        }}

        /* Hero Action Buttons */
        .hero-actions {{
            display: flex;
            gap: 10px;
            justify-content: center;
            margin-top: 10px;
        }}
        .action-btn {{
            flex: 1;
            max-width: 170px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 7px;
            padding: 10px 14px;
            border-radius: var(--radius-sm);
            font-size: 0.8rem;
            font-weight: 600;
            text-decoration: none;
            border: 1px solid var(--border-subtle);
            background: rgba(255, 255, 255, 0.06);
            color: var(--text-primary);
            cursor: pointer;
            transition: all 0.25s ease;
        }}
        .action-btn:hover {{
            transform: translateY(-2px);
            background: rgba(255, 255, 255, 0.12);
        }}
        .action-btn.primary {{
            background: var(--accent-red);
            border-color: var(--accent-red);
            box-shadow: 0 4px 14px var(--accent-red-glow);
        }}
        .action-btn.primary:hover {{
            background: var(--accent-red-hover);
        }}

        /* Search Section */
        .search-container {{
            padding: 14px 18px;
            background: var(--bg-container);
            position: sticky;
            top: 57px;
            z-index: 95;
            border-bottom: 1px solid var(--border-subtle);
        }}
        .search-wrapper {{
            position: relative;
            display: flex;
            align-items: center;
        }}
        .search-icon {{
            position: absolute;
            left: 14px;
            color: var(--text-muted);
            pointer-events: none;
        }}
        html[dir="rtl"] .search-icon {{
            left: auto;
            right: 14px;
        }}
        .search-input {{
            width: 100%;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-pill);
            padding: 10px 40px 10px 42px;
            color: var(--text-primary);
            font-family: inherit;
            font-size: 0.85rem;
            outline: none;
            transition: all 0.25s ease;
        }}
        html[dir="rtl"] .search-input {{
            padding: 10px 42px 10px 40px;
        }}
        .search-input:focus {{
            border-color: var(--accent-red);
            background: rgba(255, 255, 255, 0.09);
            box-shadow: 0 0 15px var(--accent-red-glow);
        }}
        .search-clear {{
            position: absolute;
            right: 12px;
            background: transparent;
            border: none;
            color: var(--text-muted);
            font-size: 1.1rem;
            cursor: pointer;
            display: none;
            padding: 4px;
        }}
        html[dir="rtl"] .search-clear {{
            right: auto;
            left: 12px;
        }}
        .search-clear.visible {{
            display: block;
        }}

        /* Sticky Category Navigation Pills (NordQR Style) */
        .sticky-category-nav {{
            position: sticky;
            top: 118px;
            z-index: 90;
            background: var(--bg-sticky);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border-subtle);
            padding: 9px 0;
            overflow-x: auto;
            scrollbar-width: none;
            -ms-overflow-style: none;
        }}
        .sticky-category-nav::-webkit-scrollbar {{
            display: none;
        }}
        .category-pills {{
            display: flex;
            gap: 8px;
            padding: 0 16px;
            white-space: nowrap;
        }}
        .category-pill {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 7px 14px;
            border-radius: var(--radius-pill);
            background: var(--bg-pill);
            border: 1px solid var(--border-subtle);
            color: var(--text-secondary);
            font-size: 0.78rem;
            font-weight: 500;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.25s ease;
            user-select: none;
        }}
        .category-pill:hover {{
            background: var(--bg-pill-hover);
            color: var(--text-primary);
        }}
        .category-pill.active {{
            background: var(--bg-pill-active);
            color: #ffffff;
            border-color: var(--accent-red);
            font-weight: 600;
            box-shadow: 0 2px 10px var(--accent-red-glow);
        }}

        /* Menu Content Area */
        .menu-content {{
            padding: 20px 16px;
        }}

        /* Category Section Header & Banner */
        .menu-section {{
            margin-bottom: 34px;
            scroll-margin-top: 180px;
        }}

        .category-header {{
            margin-bottom: 14px;
            position: relative;
        }}
        .category-banner-card {{
            width: 100%;
            height: 120px;
            border-radius: var(--radius-md);
            overflow: hidden;
            position: relative;
            margin-bottom: 12px;
            border: 1px solid var(--border-subtle);
            box-shadow: var(--shadow-sm);
        }}
        .category-banner-card img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: brightness(0.7);
            transition: transform 0.4s ease;
        }}
        .category-banner-card:hover img {{
            transform: scale(1.04);
        }}
        .category-banner-overlay {{
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, rgba(16, 18, 22, 0.95), transparent 70%);
            display: flex;
            align-items: flex-end;
            padding: 12px 16px;
        }}
        .category-banner-title {{
            font-size: 1.15rem;
            font-weight: 800;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 8px;
            text-shadow: 0 2px 8px rgba(0,0,0,0.8);
        }}

        .category-text-box {{
            padding: 0 4px;
        }}
        .category-title {{
            font-family: var(--font-title);
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 4px;
        }}
        .category-title-icon {{
            font-size: 1.3rem;
        }}
        .category-desc {{
            font-size: 0.8rem;
            color: var(--text-muted);
            line-height: 1.4;
        }}

        /* Dish Cards List (NordQR format) */
        .dishes-list {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}

        .dish-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            border-radius: var(--radius-md);
            padding: 12px 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            cursor: pointer;
            transition: all 0.25s ease;
            position: relative;
        }}
        .dish-card:hover {{
            background: var(--bg-card-hover);
            border-color: var(--border-red);
            transform: translateY(-2px);
            box-shadow: var(--shadow-card);
        }}

        .dish-left {{
            flex: 1;
            min-width: 0;
        }}
        .dish-title {{
            font-size: 0.96rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 3px;
            line-height: 1.3;
        }}
        .dish-desc {{
            font-size: 0.77rem;
            color: var(--text-secondary);
            line-height: 1.35;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            margin-bottom: 6px;
        }}
        .dish-price {{
            font-weight: 700;
            color: var(--accent-gold);
            font-size: 0.95rem;
            display: inline-block;
        }}

        /* Dish Right (Thumbnail Image) */
        .dish-right {{
            width: 78px;
            height: 78px;
            flex-shrink: 0;
            border-radius: var(--radius-sm);
            overflow: hidden;
            position: relative;
            background: #191c24;
            border: 1px solid var(--border-subtle);
        }}
        .dish-right img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }}
        .dish-card:hover .dish-right img {{
            transform: scale(1.08);
        }}
        .dish-img-badge {{
            position: absolute;
            bottom: 4px;
            right: 4px;
            background: rgba(0, 0, 0, 0.7);
            color: #fff;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.65rem;
        }}
        html[dir="rtl"] .dish-img-badge {{
            right: auto;
            left: 4px;
        }}

        /* Empty Search State */
        .search-empty {{
            text-align: center;
            padding: 50px 20px;
            display: none;
        }}
        .search-empty.visible {{
            display: block;
        }}
        .search-empty-icon {{
            font-size: 2.5rem;
            margin-bottom: 12px;
            opacity: 0.6;
        }}
        .search-empty-title {{
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 6px;
        }}
        .search-empty-sub {{
            font-size: 0.85rem;
            color: var(--text-muted);
        }}

        /* Interactive Photo Modal (NordQR popup_bigger) */
        .modal-overlay {{
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            z-index: 1000;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }}
        .modal-overlay.active {{
            opacity: 1;
            pointer-events: auto;
        }}

        .modal-sheet {{
            background: #14161c;
            width: 100%;
            max-width: 520px;
            border-radius: 24px 24px 0 0;
            overflow: hidden;
            box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.8);
            border: 1px solid var(--border-subtle);
            border-bottom: none;
            transform: translateY(100%);
            transition: transform 0.32s cubic-bezier(0.16, 1, 0.3, 1);
            max-height: 85vh;
            display: flex;
            flex-direction: column;
        }}
        .modal-overlay.active .modal-sheet {{
            transform: translateY(0);
        }}

        .modal-img-wrap {{
            position: relative;
            width: 100%;
            height: 250px;
            background: #000;
        }}
        .modal-img-wrap img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .modal-close-btn {{
            position: absolute;
            top: 14px;
            right: 14px;
            background: rgba(0, 0, 0, 0.65);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.2);
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 1.2rem;
            z-index: 10;
            transition: all 0.2s ease;
        }}
        html[dir="rtl"] .modal-close-btn {{
            right: auto;
            left: 14px;
        }}
        .modal-close-btn:hover {{
            background: var(--accent-red);
            transform: scale(1.1);
        }}

        .modal-body {{
            padding: 22px 20px 30px;
            overflow-y: auto;
        }}
        .modal-dish-title {{
            font-family: var(--font-title);
            font-size: 1.45rem;
            font-weight: 800;
            color: var(--text-primary);
            margin-bottom: 6px;
        }}
        html[dir="rtl"] .modal-dish-title {{
            font-family: var(--font-arabic);
        }}
        .modal-dish-price {{
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--accent-gold);
            margin-bottom: 14px;
            display: block;
        }}
        .modal-dish-desc {{
            font-size: 0.92rem;
            color: var(--text-secondary);
            line-height: 1.6;
            margin-bottom: 20px;
        }}
        .modal-footer-btn {{
            width: 100%;
            padding: 12px;
            background: var(--accent-red);
            color: #fff;
            border: none;
            border-radius: var(--radius-sm);
            font-weight: 700;
            font-size: 0.95rem;
            cursor: pointer;
            font-family: inherit;
            transition: background 0.2s ease;
        }}
        .modal-footer-btn:hover {{
            background: var(--accent-red-hover);
        }}

        /* Floating Back-to-Top Button */
        .back-to-top {{
            position: fixed;
            bottom: 24px;
            right: calc(50% - 240px);
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: var(--accent-red);
            color: #ffffff;
            border: none;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 18px var(--accent-red-glow);
            opacity: 0;
            visibility: hidden;
            transform: translateY(12px);
            transition: all 0.25s ease;
            z-index: 80;
        }}
        .back-to-top.visible {{
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }}
        @media (max-width: 540px) {{
            .back-to-top {{
                right: 18px;
            }}
        }}

        /* Footer */
        .site-footer {{
            margin-top: 40px;
            padding: 30px 20px 20px;
            text-align: center;
            border-top: 1px solid var(--border-subtle);
            background: #0b0c10;
        }}
        .footer-logo {{
            width: 60px;
            height: auto;
            margin-bottom: 12px;
            opacity: 0.9;
        }}
        .footer-title {{
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 4px;
        }}
        .footer-address {{
            font-size: 0.8rem;
            color: var(--text-secondary);
            margin-bottom: 16px;
            line-height: 1.4;
        }}
        .footer-socials {{
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-bottom: 20px;
        }}
        .footer-social-link {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border-subtle);
            color: var(--text-primary);
            text-decoration: none;
            transition: all 0.2s ease;
        }}
        .footer-social-link:hover {{
            background: var(--accent-red);
            border-color: var(--accent-red);
            transform: translateY(-2px);
        }}
        .footer-copy {{
            font-size: 0.72rem;
            color: var(--text-muted);
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            padding-top: 14px;
        }}

        /* Toast notification */
        .toast-msg {{
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(30px);
            background: #1e222d;
            color: #fff;
            padding: 10px 22px;
            border-radius: var(--radius-pill);
            border: 1px solid var(--border-red);
            box-shadow: 0 8px 24px rgba(0,0,0,0.6);
            font-size: 0.82rem;
            font-weight: 600;
            opacity: 0;
            pointer-events: none;
            transition: all 0.3s ease;
            z-index: 2000;
        }}
        .toast-msg.show {{
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }}
    </style>
</head>
<body>

    <div class="app-container">

        <!-- Top Navbar with Language Toggle -->
        <header class="top-navbar">
            <a href="#" class="brand-mini">
                <img src="images/logo.png" alt="Big House Logo">
                <span class="brand-mini-text">BIG <span>HOUSE</span></span>
            </a>

            <!-- Language Switcher -->
            <div class="lang-switch">
                <button type="button" class="lang-btn active" data-lang="fr">🇫🇷 FR</button>
                <button type="button" class="lang-btn" data-lang="ar">🇩🇿 العربية</button>
            </div>
        </header>

        <!-- Hero Section with Facade Banner & Logo -->
        <div class="hero-banner">
            <img src="images/restaurant_front.jpg" alt="Big House Restaurant & Terrasse Rouiba">
            <div class="hero-banner-overlay"></div>
        </div>

        <div class="hero-content">
            <div class="logo-emblem">
                <img src="images/logo.png" alt="Big House Logo Officiel">
            </div>

            <div class="status-badge">
                <span class="status-dot"></span>
                <span data-i18n="open_status">Ouvert aujourd'hui • 11h30 — 23h30</span>
            </div>

            <h1 class="brand-name">Big <span>House</span></h1>
            <div class="brand-subtitle" data-i18n="subtitle">Restaurant & Pizzeria au Feu de Bois</div>

            <div class="brand-slogan" data-i18n="slogan">
                « Chez nous on mange bien, On s'en souvient, Et on revient. »
            </div>

            <!-- Quick Info Chips -->
            <div class="info-grid">
                <a href="https://maps.google.com/?q=Big+House+Restaurant+Rouiba+Algeria" target="_blank" class="info-chip">
                    📍 <span data-i18n="address">16 Lot Communal, Rouiba</span>
                </a>
                <a href="tel:+213793393030" class="info-chip">
                    📞 <span dir="ltr">0793 39 30 30</span>
                </a>
                <span class="info-chip">
                    🔥 <span data-i18n="wood_fire">Four au Feu de Bois</span>
                </span>
                <span class="info-chip">
                    🌿 <span data-i18n="terrasse">Terrasse & Salons VIP</span>
                </span>
            </div>

            <!-- Hero Action Buttons -->
            <div class="hero-actions">
                <a href="https://maps.google.com/?q=Big+House+Restaurant+Rouiba+Algeria" target="_blank" class="action-btn primary">
                    🗺️ <span data-i18n="btn_maps">Itinéraire</span>
                </a>
                <a href="tel:+213793393030" class="action-btn">
                    📞 <span data-i18n="btn_call">Appeler</span>
                </a>
                <button type="button" class="action-btn" id="shareBtn">
                    📤 <span data-i18n="btn_share">Partager</span>
                </button>
            </div>
        </div>

        <!-- Sticky Search Bar -->
        <div class="search-container">
            <div class="search-wrapper">
                <span class="search-icon">🔍</span>
                <input type="text" id="searchInput" class="search-input" placeholder="Rechercher un plat, un ingrédient..." autocomplete="off">
                <button type="button" id="searchClear" class="search-clear">✕</button>
            </div>
        </div>

        <!-- Sticky Category Navigation Pills -->
        <nav class="sticky-category-nav" id="stickyNav">
            <div class="category-pills" id="categoryPills">
                <!-- Injected via JS -->
            </div>
        </nav>

        <!-- Main Menu Sections -->
        <main class="menu-content" id="menuContent">
            <!-- Injected via JS -->
        </main>

        <!-- Empty Search State -->
        <div class="search-empty" id="searchEmpty">
            <div class="search-empty-icon">🍽️</div>
            <div class="search-empty-title" data-i18n="no_result_title">Aucun plat trouvé</div>
            <div class="search-empty-sub" data-i18n="no_result_sub">Essayez un autre mot-clé ou réinitialisez la recherche.</div>
        </div>

        <!-- Interactive Dish Photo Modal (NordQR popup_bigger) -->
        <div class="modal-overlay" id="dishModal" role="dialog" aria-hidden="true">
            <div class="modal-sheet">
                <div class="modal-img-wrap">
                    <img id="modalImg" src="" alt="Photo du plat">
                    <button type="button" class="modal-close-btn" id="modalClose">✕</button>
                </div>
                <div class="modal-body">
                    <h3 class="modal-dish-title" id="modalTitle"></h3>
                    <div class="modal-dish-price" id="modalPrice"></div>
                    <p class="modal-dish-desc" id="modalDesc"></p>
                    <button type="button" class="modal-footer-btn" id="modalCloseFooter" data-i18n="modal_close">Fermer</button>
                </div>
            </div>
        </div>

        <!-- Back to Top Button -->
        <button type="button" class="back-to-top" id="backToTop" aria-label="Retour en haut">
            ▲
        </button>

        <!-- Footer -->
        <footer class="site-footer">
            <img src="images/logo.png" alt="Big House" class="footer-logo">
            <div class="footer-title">Big House Restaurant & Pizzeria</div>
            <div class="footer-address" data-i18n="footer_addr">
                16 Lot Communal, Rouiba 16000, Alger<br>
                Ouvert 7j/7 • Sam—Jeu: 11h30—23h30 • Ven: 17h00—23h30
            </div>

            <div class="footer-socials">
                <a href="https://www.instagram.com/bighouse.restaurant/" target="_blank" class="footer-social-link" title="Instagram">
                    📸
                </a>
                <a href="https://www.facebook.com/search/top?q=Big%20House%20Restaurant%20Rouiba" target="_blank" class="footer-social-link" title="Facebook">
                    👍
                </a>
                <a href="https://maps.google.com/?q=Big+House+Restaurant+Rouiba+Algeria" target="_blank" class="footer-social-link" title="Google Maps">
                    📍
                </a>
                <a href="qr-code.html" class="footer-social-link" title="QR Code Chevalet de table">
                    🔲
                </a>
            </div>

            <div class="footer-copy">
                &copy; <span id="yearSpan"></span> Big House Restaurant & Pizzeria. <span data-i18n="all_rights">Tous droits réservés.</span>
            </div>
        </footer>

    </div>

    <!-- Toast Notification -->
    <div class="toast-msg" id="toastMsg"></div>

    <!-- Client-Side Data & Script -->
    <script>
        const MENU_DATA = {categories_json};

        const TRANSLATIONS = {{
            fr: {{
                open_status: "Ouvert aujourd'hui • 11h30 — 23h30",
                subtitle: "Restaurant & Pizzeria au Feu de Bois",
                slogan: "« Chez nous on mange bien, On s'en souvient, Et on revient. »",
                address: "16 Lot Communal, Rouiba",
                wood_fire: "Four au Feu de Bois",
                terrasse: "Terrasse & Salons VIP",
                btn_maps: "Itinéraire",
                btn_call: "Appeler",
                btn_share: "Partager",
                search_placeholder: "Rechercher un plat, un ingrédient...",
                no_result_title: "Aucun plat trouvé",
                no_result_sub: "Essayez un autre mot-clé ou réinitialisez la recherche.",
                modal_close: "Fermer",
                footer_addr: "16 Lot Communal, Rouiba 16000, Alger<br>Ouvert 7j/7 • Sam—Jeu: 11h30—23h30 • Ven: 17h00—23h30",
                all_rights: "Tous droits réservés.",
                copied_toast: "Lien du menu copié !"
            }},
            ar: {{
                open_status: "مفتوح اليوم • 11:30 — 23:30",
                subtitle: "مطعم وبيتزا فاخرة على حطب الفرن",
                slogan: "« عندنا تاكل مليح، تتفكرنا، و تعاود ترجع »",
                address: "16 لوت كومينال، رويبة",
                wood_fire: "فرن تقليدي على الحطب",
                terrasse: "تراس خارجي وصالونات عائلية VIP",
                btn_maps: "الاتجاهات",
                btn_call: "اتصال",
                btn_share: "مشاركة",
                search_placeholder: "ابحث عن طبق، مكونات أو صنف...",
                no_result_title: "لم يتم العثور على أطباق",
                no_result_sub: "جرب كلمة بحث أخرى أو أعد ضبط شريط البحث.",
                modal_close: "إغلاق",
                footer_addr: "16 لوت كومينال، رويبة 16000، الجزائر العاصمة<br>مفتوح 7/7 أيام • السبت—الخميس: 11:30—23:30 • الجمعة: 17:00—23:30",
                all_rights: "جميع الحقوق محفوظة.",
                copied_toast: "تم نسخ رابط القائمة بنجاح!"
            }}
        }};

        let currentLang = localStorage.getItem('bighouse_lang') || 'fr';

        document.addEventListener('DOMContentLoaded', () => {{
            document.getElementById('yearSpan').textContent = new Date().getFullYear();

            // Initialize Language
            setLanguage(currentLang);

            // Setup Language Switcher Listeners
            document.querySelectorAll('.lang-btn').forEach(btn => {{
                btn.addEventListener('click', () => {{
                    const lang = btn.getAttribute('data-lang');
                    if (lang !== currentLang) {{
                        setLanguage(lang);
                    }}
                }});
            }});

            // Setup Search
            const searchInput = document.getElementById('searchInput');
            const searchClear = document.getElementById('searchClear');

            searchInput.addEventListener('input', () => {{
                const q = searchInput.value.trim().toLowerCase();
                if (q.length > 0) {{
                    searchClear.classList.add('visible');
                }} else {{
                    searchClear.classList.remove('visible');
                }}
                filterDishes(q);
            }});

            searchClear.addEventListener('click', () => {{
                searchInput.value = '';
                searchClear.classList.remove('visible');
                filterDishes('');
                searchInput.focus();
            }});

            // Back to top
            const backToTop = document.getElementById('backToTop');
            window.addEventListener('scroll', () => {{
                if (window.scrollY > 350) {{
                    backToTop.classList.add('visible');
                }} else {{
                    backToTop.classList.remove('visible');
                }}
            }}, {{ passive: true }});

            backToTop.addEventListener('click', () => {{
                window.scrollTo({{ top: 0, behavior: 'smooth' }});
            }});

            // Share button
            const shareBtn = document.getElementById('shareBtn');
            if (shareBtn) {{
                shareBtn.addEventListener('click', async () => {{
                    const title = currentLang === 'ar' ? 'مطعم بيغ هاوس رويبة — قائمة الطعام' : 'Big House Restaurant & Pizzeria';
                    const text = currentLang === 'ar' ? 'اكتشف القائمة الرقمية لمطعم بيغ هاوس في رويبة!' : 'Découvrez le menu digital de Big House à Rouiba !';
                    const url = window.location.href;
                    if (navigator.share) {{
                        try {{
                            await navigator.share({{ title, text, url }});
                        }} catch (e) {{
                            copyToClipboard(url);
                        }}
                    }} else {{
                        copyToClipboard(url);
                    }}
                }});
            }}

            // Setup Modal listeners
            const modal = document.getElementById('dishModal');
            const modalClose = document.getElementById('modalClose');
            const modalCloseFooter = document.getElementById('modalCloseFooter');

            const closeModal = () => {{
                modal.classList.remove('active');
                modal.setAttribute('aria-hidden', 'true');
            }};

            modalClose.addEventListener('click', closeModal);
            modalCloseFooter.addEventListener('click', closeModal);
            modal.addEventListener('click', (e) => {{
                if (e.target === modal) closeModal();
            }});
        }});

        function setLanguage(lang) {{
            currentLang = lang;
            localStorage.setItem('bighouse_lang', lang);

            // Update HTML direction & lang
            document.documentElement.lang = lang;
            document.documentElement.dir = (lang === 'ar' ? 'rtl' : 'ltr');

            // Update Lang Buttons
            document.querySelectorAll('.lang-btn').forEach(btn => {{
                if (btn.getAttribute('data-lang') === lang) {{
                    btn.classList.add('active');
                }} else {{
                    btn.classList.remove('active');
                }}
            }});

            // Update Static Texts
            const t = TRANSLATIONS[lang];
            document.querySelectorAll('[data-i18n]').forEach(el => {{
                const key = el.getAttribute('data-i18n');
                if (t[key]) {{
                    el.innerHTML = t[key];
                }}
            }});

            // Search placeholder
            document.getElementById('searchInput').placeholder = t.search_placeholder;

            // Render Nav Pills and Content
            renderCategoriesNav();
            renderMenuSections();

            // If there was an active search, re-apply
            const currentQuery = document.getElementById('searchInput').value.trim().toLowerCase();
            if (currentQuery) {{
                filterDishes(currentQuery);
            }}

            // Re-setup ScrollSpy
            setupScrollSpy();
        }}

        function renderCategoriesNav() {{
            const nav = document.getElementById('categoryPills');
            nav.innerHTML = '';

            MENU_DATA.forEach((cat, index) => {{
                const pill = document.createElement('a');
                pill.className = 'category-pill' + (index === 0 ? ' active' : '');
                pill.href = '#' + cat.id;
                pill.setAttribute('data-target', cat.id);
                const title = currentLang === 'ar' ? cat.name_ar : cat.name_fr;
                pill.innerHTML = `<span>${{cat.icon}}</span> <span>${{title}}</span>`;
                
                pill.addEventListener('click', (e) => {{
                    e.preventDefault();
                    const targetEl = document.getElementById(cat.id);
                    if (targetEl) {{
                        const offset = 175;
                        const bodyRect = document.body.getBoundingClientRect().top;
                        const elementRect = targetEl.getBoundingClientRect().top;
                        const elementPosition = elementRect - bodyRect;
                        const offsetPosition = elementPosition - offset;

                        window.scrollTo({{
                            top: offsetPosition,
                            behavior: 'smooth'
                        }});
                    }}
                }});

                nav.appendChild(pill);
            }});
        }}

        function renderMenuSections() {{
            const container = document.getElementById('menuContent');
            container.innerHTML = '';

            MENU_DATA.forEach(cat => {{
                const section = document.createElement('section');
                section.className = 'menu-section';
                section.id = cat.id;

                const catName = currentLang === 'ar' ? cat.name_ar : cat.name_fr;
                const catDesc = currentLang === 'ar' ? cat.desc_ar : cat.desc_fr;

                let bannerHtml = '';
                if (cat.banner) {{
                    bannerHtml = `
                        <div class="category-banner-card">
                            <img src="${{cat.banner}}" alt="${{catName}}" loading="lazy">
                            <div class="category-banner-overlay">
                                <div class="category-banner-title">
                                    <span>${{cat.icon}}</span> ${{catName}}
                                </div>
                            </div>
                        </div>
                    `;
                }}

                let dishesHtml = '';
                cat.items.forEach(dish => {{
                    const dishName = currentLang === 'ar' ? dish.name_ar : dish.name_fr;
                    const dishDesc = currentLang === 'ar' ? dish.desc_ar : dish.desc_fr;
                    const dishPrice = currentLang === 'ar' ? dish.price_ar : dish.price;

                    let imgHtml = '';
                    if (dish.image) {{
                        imgHtml = `
                            <div class="dish-right">
                                <img src="${{dish.image}}" alt="${{dishName}}" loading="lazy">
                                <span class="dish-img-badge">🔍</span>
                            </div>
                        `;
                    }}

                    dishesHtml += `
                        <article class="dish-card" 
                                 data-name-fr="${{dish.name_fr.toLowerCase()}}" 
                                 data-name-ar="${{dish.name_ar.toLowerCase()}}"
                                 data-desc-fr="${{dish.desc_fr.toLowerCase()}}"
                                 data-desc-ar="${{dish.desc_ar.toLowerCase()}}"
                                 data-title="${{dishName.replace(/"/g, '&quot;')}}"
                                 data-desc="${{dishDesc.replace(/"/g, '&quot;')}}"
                                 data-price="${{dishPrice}}"
                                 data-image="${{dish.image || ''}}">
                            <div class="dish-left">
                                <h4 class="dish-title">${{dishName}}</h4>
                                <p class="dish-desc">${{dishDesc}}</p>
                                <span class="dish-price">${{dishPrice}}</span>
                            </div>
                            ${{imgHtml}}
                        </article>
                    `;
                }});

                section.innerHTML = `
                    <div class="category-header">
                        ${{bannerHtml}}
                        <div class="category-text-box">
                            <h3 class="category-title">
                                <span class="category-title-icon">${{cat.icon}}</span>
                                <span>${{catName}}</span>
                            </h3>
                            <p class="category-desc">${{catDesc}}</p>
                        </div>
                    </div>
                    <div class="dishes-list">
                        ${{dishesHtml}}
                    </div>
                `;

                container.appendChild(section);
            }});

            // Attach click listeners to dish cards for modal
            document.querySelectorAll('.dish-card').forEach(card => {{
                card.addEventListener('click', () => {{
                    const img = card.getAttribute('data-image');
                    const title = card.getAttribute('data-title');
                    const desc = card.getAttribute('data-desc');
                    const price = card.getAttribute('data-price');

                    if (img) {{
                        openModal(img, title, desc, price);
                    }}
                }});
            }});
        }}

        function openModal(imgSrc, title, desc, price) {{
            const modal = document.getElementById('dishModal');
            document.getElementById('modalImg').src = imgSrc;
            document.getElementById('modalTitle').textContent = title;
            document.getElementById('modalDesc').textContent = desc;
            document.getElementById('modalPrice').textContent = price;

            modal.classList.add('active');
            modal.setAttribute('aria-hidden', 'false');
        }}

        function filterDishes(query) {{
            const sections = document.querySelectorAll('.menu-section');
            let totalVisible = 0;

            sections.forEach(sec => {{
                let secVisible = 0;
                const cards = sec.querySelectorAll('.dish-card');
                cards.forEach(card => {{
                    const nameFr = card.getAttribute('data-name-fr');
                    const nameAr = card.getAttribute('data-name-ar');
                    const descFr = card.getAttribute('data-desc-fr');
                    const descAr = card.getAttribute('data-desc-ar');

                    const match = !query || 
                                  nameFr.includes(query) || 
                                  nameAr.includes(query) || 
                                  descFr.includes(query) || 
                                  descAr.includes(query);

                    if (match) {{
                        card.style.display = 'flex';
                        secVisible++;
                        totalVisible++;
                    }} else {{
                        card.style.display = 'none';
                    }}
                }});

                if (secVisible > 0) {{
                    sec.style.display = 'block';
                }} else {{
                    sec.style.display = 'none';
                }}
            }});

            const emptyEl = document.getElementById('searchEmpty');
            if (totalVisible === 0) {{
                emptyEl.classList.add('visible');
            }} else {{
                emptyEl.classList.remove('visible');
            }}
        }}

        let spyObserver = null;
        function setupScrollSpy() {{
            if (spyObserver) spyObserver.disconnect();

            const sections = document.querySelectorAll('.menu-section');
            const pills = document.querySelectorAll('.category-pill');

            spyObserver = new IntersectionObserver((entries) => {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) {{
                        const id = entry.target.id;
                        pills.forEach(pill => {{
                            if (pill.getAttribute('data-target') === id) {{
                                pill.classList.add('active');
                                pill.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
                            }} else {{
                                pill.classList.remove('active');
                            }}
                        }});
                    }}
                }});
            }}, {{
                rootMargin: '-180px 0px -70% 0px',
                threshold: 0
            }});

            sections.forEach(sec => spyObserver.observe(sec));
        }}

        function copyToClipboard(text) {{
            if (navigator.clipboard && navigator.clipboard.writeText) {{
                navigator.clipboard.writeText(text).then(() => {{
                    showToast(TRANSLATIONS[currentLang].copied_toast);
                }}).catch(() => {{
                    showToast(text);
                }});
            }} else {{
                showToast(text);
            }}
        }}

        function showToast(msg) {{
            const el = document.getElementById('toastMsg');
            el.textContent = msg;
            el.classList.add('show');
            setTimeout(() => {{
                el.classList.remove('show');
            }}, 2800);
        }}
    </script>
</body>
</html>'''

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"index.html generated successfully! File size: {os.path.getsize(output_path)} bytes")
