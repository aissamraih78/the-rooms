path = r"C:\Users\Alone\Desktop\syntaxcraft.dev\pages\listings.vue"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

target = "        <!-- File Attachment Section -->"
button_block = """        <!-- Direct Lemon Squeezy Checkout Button -->
        <div style="display: flex; justify-content: space-between; align-items: center; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 6px; padding: 10px 14px; margin-bottom: 12px;">
          <span style="font-size: 0.85rem; color: #6b21a8; font-weight: 600;">
            ⚡ Verified Digital License & Instant Download
          </span>
          <a
            v-if="p.checkoutUrl"
            :href="p.checkoutUrl"
            target="_blank"
            class="btn btn-primary btn-sm"
            style="text-decoration: none; padding: 6px 16px; font-weight: 700; background: #7c3aed; border-color: #6d28d9;"
          >
            Buy on Lemon Squeezy (€{{ p.price }}) &rarr;
          </a>
        </div>

        <!-- File Attachment Section -->"""

if target in content:
    new_content = content.replace(target, button_block, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("SUCCESS: listings.vue updated with Buy buttons!")
else:
    print("Target not found!")

