import re

file_path = '/Users/sudeepmondal/Desktop/trwebnew/ios-app-development/index.html'
with open(file_path, 'r') as f:
    content = f.read()

replacement = """    <section id="contact" class="px-6 lg:px-12 pt-32 pb-32 bg-white relative">
        <div class="max-w-7xl mx-auto relative pt-16">
            <div class="bg-gradient-to-r from-[#2B60D3] to-[#7B42D6] rounded-[2.5rem] p-10 lg:p-16 relative shadow-[0_20px_50px_rgba(43,96,211,0.2)] flex flex-col md:flex-row items-center">
                <div class="md:w-[60%] relative z-10 text-left">
                    <h2 class="text-4xl lg:text-[3.25rem] font-black text-white leading-[1.1] mb-8 tracking-tight">
                        Tech-Powered Success<br/>
                        Awaits. Empower<br/>
                        Your Digital Journey.
                    </h2>
                    <a href="mailto:business@technorapide.com" class="inline-flex items-center gap-2 bg-white text-slate-900 px-8 py-4 rounded-full font-extrabold text-[15px] hover:scale-105 transition-transform shadow-lg">
                        Schedule a Call 
                        <span class="material-symbols-outlined font-bold text-sm">arrow_right_alt</span>
                    </a>
                </div>
                <!-- Desktop Image -->
                <div class="absolute right-4 lg:right-12 bottom-0 h-[140%] hidden md:flex items-end z-0 pointer-events-none transform origin-bottom">
                    <img src="https://res.cloudinary.com/dslw83bre/image/upload/v1771705551/front-view-young-lady-giving-empty-hand-with-her-document-Photoroom_hcc2n0.png"
                         alt="Consultant" 
                         class="h-full w-auto object-contain object-bottom drop-shadow-[0_15px_30px_rgba(0,0,0,0.3)]" />
                </div>
                <!-- Mobile Image -->
                <div class="w-full mt-10 md:hidden flex justify-center z-0 pointer-events-none">
                    <img src="https://res.cloudinary.com/dslw83bre/image/upload/v1771705551/front-view-young-lady-giving-empty-hand-with-her-document-Photoroom_hcc2n0.png"
                         alt="Consultant" 
                         class="h-80 w-auto object-contain object-bottom drop-shadow-2xl" />
                </div>
            </div>
        </div>
    </section>"""

# Find the contact section
pattern = re.compile(r'    <section id="contact".*?</section>', re.DOTALL)
new_content = pattern.sub(replacement, content, count=1)

with open(file_path, 'w') as f:
    f.write(new_content)
print("Replaced successfully.")
