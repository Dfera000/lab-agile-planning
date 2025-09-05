<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hola Mundo con Efectos</title>
    <!-- Incluye Tailwind CSS desde CDN para un diseño moderno -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Fuente Noto Sans JP de Google Fonts para un estilo más japonés -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@700&display=swap" rel="stylesheet">
    <style>
        @keyframes fadeIn {
            0% { opacity: 0; transform: scale(0.95); }
            100% { opacity: 1; transform: scale(1); }
        }
        
        @keyframes subtle-glow {
            0%, 100% { text-shadow: 0 0 5px #f43f5e, 0 0 10px #f43f5e; }
            50% { text-shadow: 0 0 10px #f43f5e, 0 0 20px #f43f5e; }
        }

        .japanese-text {
            font-family: 'Noto Sans JP', sans-serif;
            animation: fadeIn 2s ease-out;
        }

        .animated-heading {
            animation: subtle-glow 3s infinite ease-in-out;
            font-family: 'Inter', sans-serif; /* Usa una fuente moderna */
        }
    </style>
</head>
<body class="bg-gray-950 flex items-center justify-center min-h-screen text-gray-200">
    <!-- Contenedor principal centrado con un toque de estilo japonés -->
    <div class="text-center p-8 bg-gray-900 rounded-xl shadow-lg border border-red-800">
        <h1 class="text-5xl sm:text-7xl font-extrabold tracking-tight animated-heading leading-tight text-white drop-shadow-lg">
            HOLA MUNDO
        </h1>
        <p class="mt-4 text-2xl font-bold text-red-500 japanese-text">
            こんにちは世界
        </p>
        <!-- Mensaje de bienvenida con un efecto sutil -->
        <p class="mt-4 text-xl sm:text-2xl text-gray-400">
            ¡Bienvenido a tu aplicación con efectos especiales!
        </p>
    </div>
</body>
</html>
