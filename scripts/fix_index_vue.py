path = r"C:\Users\Alone\Desktop\syntaxcraft.dev\pages\index.vue"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Fix line 102: change </NuxtLink> to </a>
text = text.replace(
    "                Instant Buy ({{ tool.price }}) &rarr;\n              </NuxtLink>",
    "                Instant Buy ({{ tool.price }}) &rarr;\n              </a>"
)

# 2. Update pricing button
old_pricing = """            <NuxtLink
              :to="'/contact?package=' + pkg.id"
              class="btn"
              :class="pkg.popular ? 'btn-primary' : 'btn-secondary'"
              style="width: 100%;"
            >
              {{ pkg.cta }}
            </NuxtLink>"""

new_pricing = """            <a
              v-if="pkg.checkoutUrl"
              :href="pkg.checkoutUrl"
              target="_blank"
              class="btn"
              :class="pkg.popular ? 'btn-primary' : 'btn-secondary'"
              style="width: 100%; text-decoration: none;"
            >
              {{ pkg.cta }} &rarr;
            </a>
            <NuxtLink
              v-else
              :to="pkg.id === 'single-tool' ? '/#tools' : '/contact?package=' + pkg.id"
              class="btn"
              :class="pkg.popular ? 'btn-primary' : 'btn-secondary'"
              style="width: 100%;"
            >
              {{ pkg.cta }}
            </NuxtLink>"""

text = text.replace(old_pricing, new_pricing)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("SUCCESS: index.vue syntax fixed and pricing links connected!")

