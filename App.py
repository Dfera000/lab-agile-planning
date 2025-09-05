<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hola Mundo con Efectos</title>
    <!-- Incluye Tailwind CSS desde CDN para un diseño moderno -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @keyframes pulse-glow {
            0%, 100% {
                transform: scale(1);
                text-shadow: 0 0 5px #ff6347, 0 0 10px #ff6347, 0 0 15px #ff6347;
            }
            50% {
                transform: scale(1.1);
                text-shadow: 0 0 10px #ff6347, 0 0 20px #ff6347, 0 0 30px #ff6347;
            }
        }
        
        .animated-text {
            animation: pulse-glow 2s infinite ease-in-out;
            font-family: 'Inter', sans-serif; /* Usa una fuente moderna */
        }
    </style>
</head>
<body class="bg-slate-900 flex items-center justify-center min-h-screen text-white">
    <!-- Contenedor principal centrado -->
    <div class="text-center p-8 bg-slate-800 rounded-xl shadow-lg border border-slate-700">
        <h1 class="text-6xl sm:text-7xl font-extrabold tracking-tight animated-text leading-tight">
            HOLA MUNDO
        </h1>
        <!-- Mensaje de bienvenida con un efecto sutil -->
        <p class="mt-4 text-xl sm:text-2xl text-slate-400">
            ¡Bienvenido a tu aplicación con efectos especiales!
        </p>
    </div>
</body>
</html>
