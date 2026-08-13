from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage
import json
import random
from datetime import datetime, timedelta

CONSTRUCTION_KB = {
    "materials": {
        "bamboo": "Bamboo is excellent for villas and individual homes. It provides natural aesthetics with tensile strength of 28,000 psi. Cost: ₹1500-₹2000 per sqft installed.",
        "concrete": "Concrete is versatile for flats and high-rises. M25 grade concrete (1:1:2 mix) costs ₹5000-₹7000 per cubic meter. Add waterproofing for coastal areas.",
        "steel": "TMT bars (Fe 500) are ideal for earthquake zones. Cost: ₹60-₹80 per kg. For villas, use 12mm rods for columns and 8mm for slabs.",
        "bricks": "Fly ash bricks (230x110x75mm) cost ₹8-₹10 each. AAC blocks are lighter (₹3000-₹3500 per m³) for high-rise flats."
    },
    "property_types": {
        "villa": {
            "materials": "Recommended: Bamboo, exposed brick, large format tiles (600x1200mm). Foundation: Raft foundation for 2-3 floors.",
            "cost": "₹3000-₹5000 per sqft (basic) to ₹7000+ (premium). 3BHK (2000 sqft) ≈ ₹1-1.5 crore.",
            "time": "8-12 months for 2000 sqft villa with 5 workers."
        },
        "flat": {
            "materials": "High-rise: M40 concrete, hollow core slabs. Mid-rise: Precast panels. Finishes: Vitrified tiles (₹50-₹150/sqft).",
            "cost": "₹2500-₹4000 per sqft (basic finishes). 2BHK (1000 sqft) ≈ ₹25-40 lakhs.",
            "time": "18-24 months for 20-floor tower (100 units)."
        },
        "individual": {
            "materials": "Cost-effective: Concrete blocks, RCC frame. Roof: Filler slabs save 20% concrete. Windows: uPVC (₹800-₹1200/sqft).",
            "cost": "₹1800-₹3000 per sqft. 1BHK (600 sqft) ≈ ₹10-18 lakhs.",
            "time": "4-6 months for 600 sqft house."
        }
    },
    "configurations": {
        "1bhk": "600-800 sqft | 1 bedroom (120-150 sqft), living (200-250 sqft), kitchen (80-100 sqft), 1 bath (40-60 sqft)",
        "2bhk": "1000-1200 sqft | 2 bedrooms (120-150 sqft each), living (250-300 sqft), kitchen (100-120 sqft), 2 baths",
        "3bhk": "1500-1800 sqft | 3 bedrooms (120-150 sqft each), living (300-400 sqft), kitchen (120-150 sqft), 2-3 baths"
    },
    "safety": [
        "High-rise safety: Install safety nets every 10 floors during construction (₹15-₹20/sqft).",
        "Villa safety: Earthquake-resistant features add 10-15% cost but are mandatory in Zone III+ areas.",
        "Electrical safety: Use RCBOs (₹2000-₹3000 each) instead of MCBs for wet areas."
    ],
    "cost_factors": [
        "Location premium: Coastal areas add 15-20% for corrosion-resistant materials.",
        "Soil quality: Poor soil (black cotton) increases foundation cost by 25-40%.",
        "Floor height: Each additional floor adds ₹500-₹800/sqft for structural support."
    ],
    "unknown_responses": [
        "Our R&D team is working on expanding my knowledge. For now, I specialize in villa/flat construction queries.",
    ]
}

def get_chat_response(user_message):
    user_message = user_message.lower()
    
    # Check if message is empty or just greetings
    greetings = ['hi', 'hello', 'hey']
    if any(greet in user_message for greet in greetings):
        return "👷 Hello! I'm your Construction Assistant. How can I help with your building project today?"
    
    # Property type queries
    for prop_type in CONSTRUCTION_KB['property_types']:
        if prop_type in user_message:
            info = CONSTRUCTION_KB['property_types'][prop_type]
            return (f"For {prop_type}s:\n"
                   f"📐 Recommended Materials: {info['materials']}\n"
                   f"💰 Cost Range: {info['cost']}\n"
                   f"⏳ Construction Time: {info['time']}")

    # BHK configuration queries
    for config in CONSTRUCTION_KB['configurations']:
        if config in user_message:
            return f"Standard {config.upper()} layout:\n{CONSTRUCTION_KB['configurations'][config]}"

    # Material queries
    for material in CONSTRUCTION_KB['materials']:
        if material in user_message:
            return f"Material Info - {material.title()}:\n{CONSTRUCTION_KB['materials'][material]}"
    
    # Safety queries
    if 'safety' in user_message or 'safe' in user_message:
        return "🚧 Safety Tip:\n" + random.choice(CONSTRUCTION_KB['safety'])
    
    # Cost queries
    if any(word in user_message for word in ['cost', 'price', 'budget', 'expensive']):
        return "💵 Cost Consideration:\n" + random.choice(CONSTRUCTION_KB['cost_factors'])
    
    # Construction-related keywords that don't match specific queries
    construction_keywords = ['build', 'construct', 'house', 'home', 'floor', 'foundation', 
                           'cement', 'brick', 'design', 'plan', 'estimate']
    
    if any(keyword in user_message for keyword in construction_keywords):
        return ("🏗️ I can help with construction-related questions. "
                "Try being more specific like:\n"
                "- 'Cost to build a 3BHK villa'\n"
                "- 'Best materials for coastal areas'\n"
                "- '2BHK flat configuration'")
    
    # For completely unrelated questions
    return "🔨 " + random.choice(CONSTRUCTION_KB['unknown_responses'])

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')
        
        if not user_message:  # Initial greeting
            return JsonResponse({'response': "👷 Welcome to ConstructionBot!\nI can help with:\n- Property types (Villa/Flat/Individual)\n- BHK configurations\n- Material selection\n- Cost estimates\n\nWhat's your project requirement?"})
        
        bot_response = get_chat_response(user_message)
        
        if request.user.is_authenticated:
            ChatMessage.objects.create(
                user=request.user,
                message=user_message,
                response=bot_response,
                is_user_message=True
            )
        
        return JsonResponse({'response': bot_response})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def chat_view(request):
    chat_history = []
    if request.user.is_authenticated:
        chat_history = ChatMessage.objects.filter(user=request.user).order_by('-timestamp')[:10]
    
    return render(request, 'chat.html', {
        'chat_history': reversed(chat_history),
        'quick_questions': [
            "Safety for high-rise",
            "Concrete vs steel"
        ]
    })