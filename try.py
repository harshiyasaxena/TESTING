<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Material Expressive Portfolio</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0" />

    <style>
        /* --- 1. DESIGN TOKENS --- */
        :root {
            --surface-rgb: 253, 247, 255;
            /* Palette */
            --primary: #6750A4;
            --on-primary: #FFFFFF;
            --primary-container: #EADDFF;
            --on-primary-container: #21005D;

            --secondary: #625B71;
            --secondary-container: #E8DEF8;

            --tertiary: #7D5260;
            --tertiary-container: #FFD8E4;

            --surface: #FDF7FF;
            --surface-variant: #E7E0EC;
            --on-surface: #1D1B20;
            --outline: #79747E;

            /* --- THE BOUNCY PHYSICS ENGINE --- */
            /* The last number (1.6) controls the "overshoot" or bounce magnitude */
            --bouncy: cubic-bezier(0.175, 0.885, 0.32, 1.6);
            --standard: cubic-bezier(0.4, 0.0, 0.2, 1);

            /* Shapes */
            --radius-sm: 8px;
            --radius-md: 16px;
            --radius-lg: 24px;
            --radius-full: 999px;
        }

        /* --- 2. GLOBAL RESET --- */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Roboto', sans-serif;
            background-color: var(--surface);
            color: var(--on-surface);
            line-height: 1.6;
            overflow-x: hidden;
            padding-bottom: 80px;
        }

        a {
            text-decoration: none;
            color: inherit;
            transition: color 0.3s;
        }

        /* --- 3. NAVBAR --- */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 64px;
            background: rgba(var(--surface-rgb), 0.85);
            backdrop-filter: blur(12px);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 1.5rem;
            z-index: 1000;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
        }

        .nav-logo {
            font-weight: 900;
            font-size: 1.25rem;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 8px;
            transition: transform 0.4s var(--bouncy);
        }

        .nav-logo:hover {
            transform: scale(1.1);
        }

        .nav-links {
            display: none;
            gap: 2rem;
            font-weight: 500;
        }

        /* Bouncy Navbar Links */
        .nav-links a {
            position: relative;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            bottom: -4px;
            left: 50%;
            background-color: var(--primary);
            transition: all 0.4s var(--bouncy);
            transform: translateX(-50%);
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        @media (min-width: 768px) {
            .nav-links {
                display: flex;
            }
        }

        /* --- 4. HERO SECTION (ENTRANCE ANIMATIONS) --- */
        .hero {
            padding: 8rem 1.5rem 4rem;
            text-align: center;
            max-width: 800px;
            margin: 0 auto;
        }

        /* Staggered Bounce Entrances */
        .hero h1 {
            font-size: 3.5rem;
            line-height: 1.1;
            font-weight: 900;
            margin-bottom: 1rem;
            color: var(--on-surface);
            letter-spacing: -1px;
            animation: bounceInUp 0.8s var(--bouncy) forwards;
            opacity: 0;
            transform: translateY(30px);
        }

        .hero p {
            font-size: 1.25rem;
            color: var(--secondary);
            max-width: 600px;
            margin: 0 auto 2rem;
            animation: bounceInUp 0.8s var(--bouncy) 0.1s forwards;
            opacity: 0;
            transform: translateY(30px);
        }

        .hero-btns {
            display: flex;
            gap: 1rem;
            justify-content: center;
            animation: bounceInUp 0.8s var(--bouncy) 0.2s forwards;
            opacity: 0;
            transform: translateY(30px);
        }

        /* --- 5. BENTO GRID --- */
        .layout-section {
            padding: 4rem 1.5rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-title {
            font-size: 1.75rem;
            margin-bottom: 2rem;
            font-weight: 700;
            text-align: center;
        }

        .bento-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1rem;
        }

        @media (min-width: 700px) {
            .bento-grid {
                grid-template-columns: repeat(3, 1fr);
                grid-template-rows: repeat(2, 300px);
            }

            .bento-item:nth-child(1) {
                grid-column: span 2;
            }

            .bento-item:nth-child(2) {
                grid-row: span 2;
            }
        }

        .bento-item {
            background: var(--surface-variant);
            border-radius: var(--radius-lg);
            padding: 2rem;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            transition: transform 0.4s var(--bouncy), box-shadow 0.4s var(--standard);
            position: relative;
            overflow: hidden;
            min-height: 250px;
            cursor: pointer;
        }

        /* HOVER EFFECT: Lift and Bounce */
        .bento-item:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.1);
            z-index: 2;
        }

        .card-1 {
            background: var(--primary-container);
            color: var(--on-primary-container);
        }

        .card-2 {
            background: var(--secondary);
            color: white;
        }

        .card-3 {
            background: #FFD8E4;
            color: #31111D;
        }

        .bento-icon {
            font-size: 3rem;
            margin-bottom: auto;
            opacity: 0.8;
            transition: transform 0.4s var(--bouncy);
        }

        .bento-item:hover .bento-icon {
            transform: scale(1.2) rotate(-5deg);
        }

        .card-1:hover .bento-icon {
            /* We rotate less (-3deg) and move it right (translateX) so it stays inside */
            transform: scale(1.15) rotate(-3deg) translateX(10px);
        }

        /* --- 6. TIC TAC TOE GAME --- */
        .game-section {
            padding: 4rem 1.5rem;
            background: var(--surface-variant);
            border-radius: var(--radius-lg);
            margin: 2rem 1rem;
            text-align: center;
        }

        .game-board {
            display: grid;
            grid-template-columns: repeat(3, 100px);
            grid-template-rows: repeat(3, 100px);
            gap: 12px;
            margin: 2rem auto;
            justify-content: center;
            position: relative;
            width: max-content;
        }

        .cell {
            width: 100px;
            height: 100px;
            background: var(--surface);
            border-radius: var(--radius-md);
            border: none;
            font-size: 3.5rem;
            font-weight: 900;
            cursor: pointer;
            color: var(--on-surface);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s var(--bouncy), background-color 0.2s;
            box-shadow: 0 4px 0 rgba(0, 0, 0, 0.05);
        }

        /* Hover Pop */
        .cell:hover {
            background: #fff;
            transform: scale(1.08);
            z-index: 10;
        }

        .cell:active {
            transform: scale(0.9);
        }

        /* Animation when X or O appears */
        .cell.x,
        .cell.o {
            animation: popIn 0.5s var(--bouncy) forwards;
        }

        .cell.x {
            color: var(--primary);
        }

        .cell.o {
            color: var(--tertiary);
        }

        .strike-line {
            position: absolute;
            background-color: var(--on-surface);
            transition: width 0.6s var(--bouncy), height 0.6s var(--bouncy);
            border-radius: 4px;
            z-index: 20;
            pointer-events: none;
            transform-origin: center;
        }

        /* Default Hidden */
        .strike-line {
            width: 0;
            height: 8px;
            transform-origin: left center;
        }

        /* Wins */
        .win-row-0 {
            top: 16%;
            left: 0;
            width: 100%;
        }

        .win-row-1 {
            top: 50%;
            left: 0;
            width: 100%;
            transform: translateY(-50%);
        }

        .win-row-2 {
            bottom: 16%;
            left: 0;
            width: 100%;
        }

        .win-col-0 {
            left: 16%;
            top: 0;
            height: 100%;
            width: 8px;
        }

        .win-col-1 {
            left: 50%;
            top: 0;
            height: 100%;
            width: 8px;
            transform: translateX(-50%);
        }

        .win-col-2 {
            right: 16%;
            top: 0;
            height: 100%;
            width: 8px;
        }

        .win-diag-0 {
            top: 0;
            left: 0;
            width: 140%;
            height: 8px;
            transform: rotate(45deg);
            transform-origin: 10px 10px;
        }

        .win-diag-1 {
            bottom: 0;
            left: 0;
            width: 140%;
            height: 8px;
            transform: rotate(-45deg);
            transform-origin: 10px -10px;
        }

        /* --- UPDATED AVATAR & NAME INPUT CSS --- */
        .avatar-wrapper {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            /* More space between players */
            margin-bottom: 2rem;
            /* REMOVED background color so the label masks blend in */
            padding: 0.5rem;
        }

        .player-col {
            display: flex;
            flex-direction: column;
            gap: 12px;
            align-items: center;
        }

        /* Ensure inputs take full width of their column */
        .player-col .input-group {
            width: 100%;
            margin-bottom: 0;
            /* Remove extra margin */
        }

        /* Standard left-aligned text looks best for floating labels */
        .player-col .m3-field {
            text-align: left;
            font-size: 0.95rem;
        }

        .avatar-list {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .avatar-btn {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: 1px solid var(--outline);
            background: transparent;
            font-size: 1.2rem;
            cursor: pointer;
            transition: all 0.3s var(--bouncy);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .avatar-btn:hover {
            transform: scale(1.1);
            background: var(--surface-variant);
        }

        .avatar-btn.selected {
            background-color: var(--primary);
            border-color: var(--primary);
            transform: scale(1.15);
            box-shadow: 0 4px 10px rgba(103, 80, 164, 0.3);
        }

        @media (max-width: 400px) {
            .avatar-wrapper {
                grid-template-columns: 1fr;
            }
        }

        /* --- LEADERBOARD PODIUM CSS --- */
        .leaderboard-container {
            margin-top: 2rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--outline);
            width: 100%;
        }

        .podium {
            display: flex;
            justify-content: center;
            align-items: flex-end;
            /* Align to bottom so bars grow up */
            gap: 1.5rem;
            height: 180px;
        }

        .podium-step {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100px;
            position: relative;
            transition: all 0.5s var(--bouncy);
        }

        .podium-avatar {
            font-size: 2.5rem;
            margin-bottom: 8px;
            filter: drop-shadow(0 4px 4px rgba(0, 0, 0, 0.1));
            transition: transform 0.3s var(--bouncy);
        }

        .podium-bar {
            width: 100%;
            border-radius: var(--radius-md) var(--radius-md) 0 0;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            align-items: center;
            padding-bottom: 10px;
            color: white;
            font-weight: 700;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* 1st Place Styling */
        .step-1 .podium-bar {
            height: 100px;
            background: linear-gradient(135deg, #FFD700, #FDB931);
            z-index: 2;
        }

        .icon-crown {
            position: absolute;
            top: -40px;
            font-size: 1.5rem;
            opacity: 0;
            transform: scale(0.5);
            transition: all 0.4s var(--bouncy);
        }

        .step-1 .icon-crown {
            opacity: 1;
            transform: scale(1);
            animation: bounceInUp 1s infinite alternate;
        }

        /* 2nd Place Styling */
        .step-2 .podium-bar {
            height: 70px;
            background: linear-gradient(135deg, #E0E0E0, #BDBDBD);
        }

        .podium-name {
            margin-top: 8px;
            font-size: 0.9rem;
            font-weight: 500;
            text-align: center;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 100%;
        }

        .score {
            font-size: 1.5rem;
            line-height: 1;
        }

        .rank {
            font-size: 0.75rem;
            margin-bottom: 4px;
            opacity: 0.8;
        }

        /* --- 7. FORM SECTION --- */
        .form-section {
            max-width: 600px;
            margin: 4rem auto;
            padding: 0 1.5rem;
        }

        .input-group {
            position: relative;
            margin-bottom: 24px;
        }

        .m3-field {
            width: 100%;
            padding: 16px;
            border: 2px solid transparent;
            box-shadow: 0 0 0 1px var(--outline);
            border-radius: var(--radius-sm);
            background: transparent;
            font-size: 1rem;
            color: var(--on-surface);
            transition: all 0.3s var(--bouncy);
        }

        .m3-field:focus {
            box-shadow: 0 0 0 0 transparent;
            /* remove outline shadow */
            border-color: var(--primary);
            padding: 16px 20px;
            /* Slight expansion */
            outline: none;
            transform: scale(1.02);
            /* Focus Pop */
        }

        .m3-label {
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            background: var(--surface);
            padding: 0 4px;
            color: var(--outline);
            transition: 0.3s var(--bouncy);
            pointer-events: none;
        }

        .m3-field:focus+.m3-label,
        .m3-field:not(:placeholder-shown)+.m3-label {
            top: 0;
            font-size: 0.8rem;
            color: var(--primary);
            font-weight: 700;
            transform: translateY(-50%) scale(1.1);
            /* Label pop */
        }

        /* --- 8. BUTTONS --- */
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0 28px;
            height: 52px;
            border-radius: var(--radius-full);
            border: none;
            font-weight: 700;
            letter-spacing: 0.5px;
            cursor: pointer;
            transition: transform 0.4s var(--bouncy), box-shadow 0.4s var(--bouncy);
            position: relative;
            overflow: hidden;
        }

        .btn:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 8px 15px rgba(103, 80, 164, 0.3);
        }

        .btn:active {
            transform: translateY(2px) scale(0.95);
            box-shadow: 0 2px 5px rgba(103, 80, 164, 0.2);
        }

        .btn-filled {
            background: var(--primary);
            color: var(--on-primary);
            width: 100%;
        }

        .btn-tonal {
            background: var(--secondary-container);
            color: var(--on-primary-container);
        }

        /* --- 9. TOAST --- */
        .toast {
            position: fixed;
            bottom: -150px;
            left: 50%;
            transform: translateX(-50%);
            background: var(--on-surface);
            color: var(--surface);
            padding: 1.25rem 2.5rem;
            border-radius: var(--radius-full);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
            z-index: 2000;
            display: flex;
            align-items: center;
            gap: 12px;
            transition: bottom 0.6s var(--bouncy);
            /* Bouncy entrance */
            min-width: 320px;
            justify-content: center;
            font-weight: 500;
        }

        .toast.show {
            bottom: 40px;
        }

        .toast-icon {
            font-size: 1.75rem;
            color: #4caf50;
            animation: popIn 0.5s var(--bouncy);
        }

        /* --- 10. KEYFRAMES --- */
        @keyframes bounceInUp {
            from {
                opacity: 0;
                transform: translateY(50px) scale(0.9);
            }

            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        @keyframes popIn {
            0% {
                opacity: 0;
                transform: scale(0);
            }

            60% {
                transform: scale(1.3);
            }

            /* Big Overshoot */
            100% {
                opacity: 1;
                transform: scale(1);
            }
        }

        /* --- PRELOADER CSS --- */
        #preloader {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: var(--surface);
            z-index: 9999;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: opacity 0.5s ease-out, visibility 0.5s;
        }

        .loader-container {
            display: flex;
            gap: 12px;
        }

        .dot {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            animation: jump 0.6s var(--bouncy) infinite alternate;
        }

        .dot-1 {
            background-color: var(--primary);
            animation-delay: 0s;
        }

        .dot-2 {
