#!/usr/bin/env python3
"""Script to add actual images to project cards"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the replacements
replacements = [
    # Project 1: Last Drop
    (
        '<div class="project-image">\n          �\n          <span class="project-status">LIVE</span>\n        </div>',
        '<div class="project-image">\n          <img src="project-images/last-drop.png" alt="Last Drop Runner Game" onerror="this.parentElement.innerHTML=\'<div class=\\\'project-image-placeholder\\\'>💧</div><span class=\\\'project-status\\\'>LIVE</span>\'">\n          <span class="project-status">LIVE</span>\n        </div>'
    ),
    # Project 2: L'Oréal Routine Builder
    (
        '<div class="project-image">\n          💄\n          <span class="project-status">LIVE</span>\n        </div>',
        '<div class="project-image">\n          <img src="project-images/routine-builder.png" alt="L\'Oréal Routine Builder" onerror="this.parentElement.innerHTML=\'<div class=\\\'project-image-placeholder\\\'>💄</div><span class=\\\'project-status\\\'>LIVE</span>\'">\n          <span class="project-status">LIVE</span>\n        </div>'
    ),
    # Project 3: L'Oréal Beauty Chatbot
    (
        '<div class="project-image">\n          💬\n          <span class="project-status">LIVE</span>\n        </div>',
        '<div class="project-image">\n          <img src="project-images/beauty-chatbot.png" alt="L\'Oréal Beauty Assistant" onerror="this.parentElement.innerHTML=\'<div class=\\\'project-image-placeholder\\\'>💬</div><span class=\\\'project-status\\\'>LIVE</span>\'">\n          <span class="project-status">LIVE</span>\n        </div>'
    ),
    # Project 4: NASA Space Explorer
    (
        '<div class="project-image">\n          🚀\n          <span class="project-status">LIVE</span>\n        </div>',
        '<div class="project-image">\n          <img src="project-images/nasa-explorer.png" alt="NASA Space Explorer" onerror="this.parentElement.innerHTML=\'<div class=\\\'project-image-placeholder\\\'>🚀</div><span class=\\\'project-status\\\'>LIVE</span>\'">\n          <span class="project-status">LIVE</span>\n        </div>'
    ),
]

# Apply replacements
for old, new in replacements:
    content = content.replace(old, new)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Updated HTML with image tags!")
print("\n📸 Next steps:")
print("1. Take screenshots of your projects")
print("2. Save them in the 'project-images' folder with these names:")
print("   - last-drop.png")
print("   - routine-builder.png")
print("   - beauty-chatbot.png")
print("   - nasa-explorer.png")
print("   - intel-event.png")
print("   - intel-timeline.png")
print("\n💡 Tip: Until you add images, the emojis will show as fallbacks!")
