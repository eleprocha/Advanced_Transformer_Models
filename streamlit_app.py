import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Transformer Models Presentation",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# HTML content for the presentation
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transformer Models Presentation</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .presentation-container {
            width: 90vw;
            height: 90vh;
            background: white;
            border-radius: 10px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
        }

        .slide {
            width: 100%;
            height: 100%;
            position: absolute;
            display: none;
            padding: 60px 80px;
            background: white;
        }

        .slide.active {
            display: flex;
            flex-direction: column;
            animation: fadeIn 0.5s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateX(20px); }
            to { opacity: 1; transform: translateX(0); }
        }

        .slide-header {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #FFD700;
            padding: 30px 40px;
            margin: -60px -80px 40px -80px;
            border-bottom: 5px solid #FFD700;
        }

        .slide-header h1 {
            font-size: 48px;
            font-weight: 700;
            margin-bottom: 10px;
        }

        .slide-header h2 {
            font-size: 36px;
            font-weight: 600;
            margin-bottom: 5px;
        }

        .slide-header p {
            font-size: 20px;
            color: #FFF9C4;
            margin-top: 10px;
        }

        .content {
            flex: 1;
            overflow-y: auto;
            color: #1e3c72;
        }

        h3 {
            color: #1e3c72;
            font-size: 32px;
            margin: 25px 0 15px 0;
            border-left: 6px solid #FFD700;
            padding-left: 20px;
        }

        .model-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
            margin: 30px 0;
        }

        .model-card {
            background: linear-gradient(135deg, #2a5298 0%, #1e3c72 100%);
            color: white;
            padding: 25px;
            border-radius: 10px;
            border: 3px solid #FFD700;
            transition: transform 0.3s ease;
        }

        .model-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(255, 215, 0, 0.3);
        }

        .model-card h4 {
            color: #FFD700;
            font-size: 24px;
            margin-bottom: 15px;
        }

        .model-card p {
            font-size: 16px;
            line-height: 1.6;
        }

        ul {
            margin: 20px 0 20px 40px;
            line-height: 2;
        }

        li {
            font-size: 20px;
            margin: 10px 0;
            color: #2a5298;
        }

        li strong {
            color: #1e3c72;
        }

        .lab-section {
            background: #FFF9C4;
            border-left: 6px solid #1e3c72;
            padding: 25px;
            margin: 20px 0;
            border-radius: 5px;
        }

        .lab-section h4 {
            color: #1e3c72;
            font-size: 24px;
            margin-bottom: 15px;
        }

        .lab-section p {
            color: #2a5298;
            font-size: 18px;
            line-height: 1.7;
        }

        .controls {
            position: absolute;
            bottom: 30px;
            right: 30px;
            display: flex;
            gap: 15px;
            z-index: 100;
        }

        button {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #FFD700;
            border: 2px solid #FFD700;
            padding: 12px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        button:hover {
            background: #FFD700;
            color: #1e3c72;
            transform: scale(1.05);
        }

        button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        .slide-number {
            position: absolute;
            bottom: 30px;
            left: 30px;
            background: #1e3c72;
            color: #FFD700;
            padding: 10px 20px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 16px;
        }

        .highlight-box {
            background: linear-gradient(135deg, #2a5298 0%, #1e3c72 100%);
            color: white;
            padding: 20px 30px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 6px solid #FFD700;
        }

        .two-column {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="presentation-container">
        <!-- Slide 1: Title -->
        <div class="slide active">
            <div class="slide-header">
                <h1>🤖 Advanced Transformer Models</h1>
                <p>Getting Started with Decoder, Encoder, and Encoder-Decoder Architectures</p>
            </div>
            <div class="content" style="display: flex; justify-content: center; align-items: center;">
                <div style="text-align: center;">
                    <h2 style="color: #1e3c72; font-size: 42px; margin-bottom: 30px;">Three Transformer Families</h2>
                    <div style="display: flex; justify-content: space-around; align-items: center; gap: 40px;">
                        <div style="text-align: center;">
                            <div style="font-size: 80px; color: #FFD700;">📝</div>
                            <h3 style="border: none; padding: 0; margin-top: 15px;">GPT</h3>
                            <p style="color: #2a5298; font-size: 20px;">Decoder-Only</p>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 80px; color: #FFD700;">🔍</div>
                            <h3 style="border: none; padding: 0; margin-top: 15px;">BERT</h3>
                            <p style="color: #2a5298; font-size: 20px;">Encoder-Only</p>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 80px; color: #FFD700;">🌐</div>
                            <h3 style="border: none; padding: 0; margin-top: 15px;">Seq2Seq</h3>
                            <p style="color: #2a5298; font-size: 20px;">Encoder-Decoder</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 2: Overview -->
        <div class="slide">
            <div class="slide-header">
                <h2>📋 Learning Objectives</h2>
            </div>
            <div class="content">
                <div class="model-grid">
                    <div class="model-card">
                        <h4>🎯 Decoder Models (GPT)</h4>
                        <p>Best for generating text: chatbots, story writing, and autocomplete applications</p>
                    </div>
                    <div class="model-card">
                        <h4>🎯 Encoder Models (BERT)</h4>
                        <p>Best for understanding tasks: search engines, sentiment analysis, and question answering</p>
                    </div>
                    <div class="model-card">
                        <h4>🎯 Encoder-Decoder Models</h4>
                        <p>Best for translation and tasks requiring input-output sequence mapping</p>
                    </div>
                </div>

                <h3>Key Concepts You'll Master</h3>
                <ul>
                    <li><strong>Attention Mechanisms:</strong> Queries (Q), Keys (K), and Values (V) for capturing word relationships</li>
                    <li><strong>Positional Encoding:</strong> Preserving sequence order in parallel processing</li>
                    <li><strong>Masking Strategies:</strong> Guiding model learning for different tasks</li>
                    <li><strong>Hands-on Implementation:</strong> Building GPT, BERT, and translation models</li>
                </ul>
            </div>
        </div>

        <!-- Slide 3: Decoder Models -->
        <div class="slide">
            <div class="slide-header">
                <h2>📝 Decoder Models (GPT-like)</h2>
                <p>Autoregressive Text Generation</p>
            </div>
            <div class="content">
                <div class="highlight-box">
                    <h4 style="color: #FFD700; font-size: 24px; margin-bottom: 10px;">💡 Real-World Example</h4>
                    <p style="font-size: 20px;">You type: "How are ___" → The system suggests: "you"</p>
                </div>

                <h3>Key Training Components</h3>
                <div class="two-column">
                    <div>
                        <h4 style="color: #1e3c72; font-size: 22px; margin-bottom: 15px;">🎭 Causal Masking</h4>
                        <ul style="margin-left: 20px;">
                            <li>Hides future tokens during training</li>
                            <li>Model only sees previous words</li>
                            <li>Ensures autoregressive behavior</li>
                        </ul>
                    </div>
                    <div>
                        <h4 style="color: #1e3c72; font-size: 22px; margin-bottom: 15px;">⚙️ Implementation</h4>
                        <ul style="margin-left: 20px;">
                            <li>Build from scratch in PyTorch</li>
                            <li>Use GPT2LMHeadModel (Hugging Face)</li>
                            <li>Fine-tune with Trainer API</li>
                            <li>Generate with pipeline</li>
                        </ul>
                    </div>
                </div>

                <div class="lab-section">
                    <h4>🔬 Applications</h4>
                    <p>Chatbots • Story Writing • Code Completion • Text Summarization • Creative Writing</p>
                </div>
            </div>
        </div>

        <!-- Slide 4: Encoder Models -->
        <div class="slide">
            <div class="slide-header">
                <h2>🔍 Encoder-Only Models (BERT)</h2>
                <p>Bidirectional Context Understanding</p>
            </div>
            <div class="content">
                <div class="highlight-box">
                    <h4 style="color: #FFD700; font-size: 24px; margin-bottom: 10px;">🔄 Key Difference from GPT</h4>
                    <p style="font-size: 20px;">BERT captures context from BOTH directions simultaneously</p>
                </div>

                <h3>Pretraining Tasks</h3>
                <div class="two-column">
                    <div class="lab-section">
                        <h4>🎭 Masked Language Modeling (MLM)</h4>
                        <p><strong>Goal:</strong> Randomly mask tokens and train the model to recover them</p>
                        <p style="margin-top: 10px;"><strong>Example:</strong> "The dog is chasing the ___" → Predict "cat"</p>
                        <p style="margin-top: 10px;">Forces bidirectional understanding of context</p>
                    </div>
                    <div class="lab-section">
                        <h4>🔗 Next Sentence Prediction (NSP)</h4>
                        <p><strong>Goal:</strong> Detect if sentence B follows sentence A</p>
                        <p style="margin-top: 10px;"><strong>Benefit:</strong> Understands relationships between sentences</p>
                        <p style="margin-top: 10px;">Useful for Q&A and summarization tasks</p>
                    </div>
                </div>

                <h3>Data Preparation in PyTorch</h3>
                <ul>
                    <li><strong>Tokenization:</strong> Splits text into subword tokens with [CLS]/[SEP]</li>
                    <li><strong>Segment IDs:</strong> Identifies tokens from sentence A vs. sentence B</li>
                    <li><strong>Attention Masks:</strong> Distinguishes real tokens from padding</li>
                </ul>
            </div>
        </div>

        <!-- Slide 5: Encoder-Decoder Models -->
        <div class="slide">
            <div class="slide-header">
                <h2>🌐 Encoder-Decoder Models</h2>
                <p>Sequence-to-Sequence Translation</p>
            </div>
            <div class="content">
                <div class="highlight-box">
                    <h4 style="color: #FFD700; font-size: 24px; margin-bottom: 10px;">🎯 Best of Both Worlds</h4>
                    <p style="font-size: 20px;">Combines encoder understanding + decoder generation capabilities</p>
                </div>

                <h3>Architecture Components</h3>
                <div class="model-grid" style="grid-template-columns: 1fr 1fr; margin: 30px 0;">
                    <div class="model-card">
                        <h4>📖 Encoder</h4>
                        <p style="margin-bottom: 15px;">Reads the full source sequence</p>
                        <p><strong>Example:</strong> Processes entire German sentence</p>
                    </div>
                    <div class="model-card">
                        <h4>✍️ Decoder</h4>
                        <p style="margin-bottom: 15px;">Generates output word by word</p>
                        <p><strong>Example:</strong> Produces English translation step by step</p>
                    </div>
                </div>

                <h3>🔗 Cross-Attention Bridge</h3>
                <div class="lab-section">
                    <p>The decoder looks at BOTH:</p>
                    <ul style="margin-left: 30px; margin-top: 10px;">
                        <li>Past words it has already generated</li>
                        <li>Full source sentence from the encoder</li>
                    </ul>
                </div>

                <h3>Applications</h3>
                <p style="font-size: 20px; color: #2a5298; margin: 20px 0;">Translation • Summarization • Dialogue Systems • Code-to-Text • Any sequence mapping task</p>
            </div>
        </div>

        <!-- Slide 6: Lab 1 -->
        <div class="slide">
            <div class="slide-header">
                <h2>🔬 Lab 1: Decoder Causal Language Models</h2>
                <p>Building GPT-like Text Generation</p>
            </div>
            <div class="content">
                <div class="lab-section">
                    <h4>🎯 Lab Focus: Causal Language Modeling</h4>
                    <p>Predicting the next word given previous ones</p>
                </div>

                <h3>Key Concepts</h3>
                <ul>
                    <li><strong>Dataset Processing:</strong> IMDB reviews → tokens → numerical vocabulary</li>
                    <li><strong>Causal Masking:</strong> Each word can only attend to previous words, not future ones</li>
                    <li><strong>Positional Encoding:</strong> Trainable embeddings to learn word order</li>
                    <li><strong>Autoregressive Generation:</strong> Generate text one token at a time</li>
                </ul>

                <h3>Training Pipeline</h3>
                <div class="two-column" style="margin-top: 25px;">
                    <div class="highlight-box">
                        <h4 style="color: #FFD700; margin-bottom: 15px;">📚 Data Preparation</h4>
                        <p>• Break text into tokens</p>
                        <p>• Convert to numbers</p>
                        <p>• Create vocabulary</p>
                    </div>
                    <div class="highlight-box">
                        <h4 style="color: #FFD700; margin-bottom: 15px;">🚀 Model Training</h4>
                        <p>• Apply causal masking</p>
                        <p>• Train on next-word prediction</p>
                        <p>• Test with inference prompts</p>
                    </div>
                </div>

                <div class="lab-section" style="margin-top: 30px;">
                    <h4>💡 Why GPT is Powerful</h4>
                    <p>Perfect for creative tasks: writing, summarizing, answering prompts, and code generation</p>
                </div>
            </div>
        </div>

        <!-- Slide 7: Lab 2 -->
        <div class="slide">
            <div class="slide-header">
                <h2>🔬 Lab 2: Pretraining BERT Models</h2>
                <p>Encoder-Only Architecture</p>
            </div>
            <div class="content">
                <div class="lab-section">
                    <h4>🎯 Lab Focus: Reading and Understanding</h4>
                    <p>BERT looks at entire sentences bidirectionally to learn deep context</p>
                </div>

                <h3>Two Pretraining Tasks</h3>
                <div class="model-grid" style="grid-template-columns: 1fr 1fr;">
                    <div class="model-card">
                        <h4>🎭 Masked Language Modeling</h4>
                        <p style="margin-bottom: 10px;"><strong>Task:</strong> Hide words and predict them</p>
                        <p style="margin-bottom: 10px;"><strong>Example:</strong> "The dog is chasing the ___"</p>
                        <p><strong>Result:</strong> Forces left AND right context usage</p>
                    </div>
                    <div class="model-card">
                        <h4>🔗 Next Sentence Prediction</h4>
                        <p style="margin-bottom: 10px;"><strong>Task:</strong> Does sentence B follow A?</p>
                        <p style="margin-bottom: 10px;"><strong>Benefit:</strong> Learns sentence relationships</p>
                        <p><strong>Use Case:</strong> Q&A and summarization</p>
                    </div>
                </div>

                <h3>Segment Embeddings</h3>
                <div class="highlight-box">
                    <p style="font-size: 20px;">Since BERT works with sentence pairs, segment embeddings mark:</p>
                    <ul style="margin-left: 30px; margin-top: 15px; color: white;">
                        <li>"This token belongs to sentence A"</li>
                        <li>"This token belongs to sentence B"</li>
                    </ul>
                </div>

                <div class="lab-section" style="margin-top: 25px;">
                    <h4>🎓 What You Learn</h4>
                    <p>BERT creates representations for <strong>understanding</strong> language, not just generating it. Test on sentence-pair tasks and masked word prediction.</p>
                </div>
            </div>
        </div>

        <!-- Slide 8: Lab 3 -->
        <div class="slide">
            <div class="slide-header">
                <h2>🔬 Lab 3: Transformer for Translation</h2>
                <p>Encoder-Decoder Architecture</p>
            </div>
            <div class="content">
                <div class="lab-section">
                    <h4>🌍 Combining Both Worlds</h4>
                    <p>Encoder (like BERT) + Decoder (like GPT) = Full Seq2Seq Transformer</p>
                </div>

                <h3>How It Works</h3>
                <div class="highlight-box">
                    <h4 style="color: #FFD700; font-size: 22px; margin-bottom: 15px;">🔄 Translation Process</h4>
                    <p style="font-size: 19px; line-height: 1.8;">
                        <strong>Step 1:</strong> Encoder reads the full German sentence<br>
                        <strong>Step 2:</strong> Decoder generates English words one by one<br>
                        <strong>Step 3:</strong> Decoder checks both past generated words AND the source sentence
                    </p>
                </div>

                <h3>Architecture Components</h3>
                <ul>
                    <li><strong>Encoder:</strong> Reads full source sentence (e.g., German)</li>
                    <li><strong>Decoder:</strong> Generates target sentence word by word (e.g., English)</li>
                    <li><strong>Cross-Attention:</strong> Decoder attends to encoder's output</li>
                    <li><strong>Self-Attention:</strong> Decoder attends to previously generated words</li>
                </ul>

                <h3>Training Process</h3>
                <div class="lab-section">
                    <p><strong>Compare:</strong> Prediction vs. actual word</p>
                    <p><strong>Compute:</strong> Loss (error measurement)</p>
                    <p><strong>Adjust:</strong> Model parameters to minimize loss</p>
                </div>

                <h3>Beyond Translation</h3>
                <p style="font-size: 20px; color: #2a5298; margin-top: 20px;">Summarization • Dialogue • Code-to-Text • Any sequence-to-sequence mapping</p>
            </div>
        </div>

        <!-- Slide 9: Summary -->
        <div class="slide">
            <div class="slide-header">
                <h2>📚 Summary: Choosing the Right Model</h2>
            </div>
            <div class="content">
                <div class="model-grid">
                    <div class="model-card">
                        <h4>📝 Decoder (GPT)</h4>
                        <p style="margin-bottom: 10px;"><strong>When:</strong> Need to generate text</p>
                        <p style="margin-bottom: 10px;"><strong>How:</strong> Causal masking, autoregressive</p>
                        <p><strong>Use:</strong> Chatbots, writing, autocomplete</p>
                    </div>
                    <div class="model-card">
                        <h4>🔍 Encoder (BERT)</h4>
                        <p style="margin-bottom: 10px;"><strong>When:</strong> Need to understand text</p>
                        <p style="margin-bottom: 10px;"><strong>How:</strong> Bidirectional, MLM + NSP</p>
                        <p><strong>Use:</strong> Search, sentiment, Q&A</p>
                    </div>
                    <div class="model-card">
                        <h4>🌐 Encoder-Decoder</h4>
                        <p style="margin-bottom: 10px;"><strong>When:</strong> Map input to output</p>
                        <p style="margin-bottom: 10px;"><strong>How:</strong> Cross-attention bridge</p>
                        <p><strong>Use:</strong> Translation, summarization</p>
                    </div>
                </div>

                <h3>Key Takeaways</h3>
                <ul>
                    <li><strong>Attention Mechanisms:</strong> Q, K, V help models capture word relationships</li>
                    <li><strong>Positional Encoding:</strong> Preserves sequence order in parallel processing</li>
                    <li><strong>Masking Strategies:</strong> Causal for generation, bidirectional for understanding</li>
                    <li><strong>Hands-on Experience:</strong> Build and train models in PyTorch with Hugging Face</li>
                </ul>

                <div class="highlight-box" style="margin-top: 30px; text-align: center;">
                    <h4 style="color: #FFD700; font-size: 28px;">🎓 Ready to Build Transformers!</h4>
                    <p style="font-size: 20px; margin-top: 10px;">You now understand when to use each architecture and how to implement them</p>
                </div>
            </div>
        </div>

        <!-- Navigation -->
        <div class="slide-number">
            <span id="currentSlide">1</span> / <span id="totalSlides">9</span>
        </div>

        <div class="controls">
            <button id="prevBtn" onclick="changeSlide(-1)">← Previous</button>
            <button id="nextBtn" onclick="changeSlide(1)">Next →</button>
        </div>
    </div>

    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        
        document.getElementById('totalSlides').textContent = totalSlides;

        function showSlide(n) {
            slides[currentSlide].classList.remove('active');
            currentSlide = (n + totalSlides) % totalSlides;
            slides[currentSlide].classList.add('active');
            
            document.getElementById('currentSlide').textContent = currentSlide + 1;
            
            document.getElementById('prevBtn').disabled = currentSlide === 0;
            document.getElementById('nextBtn').disabled = currentSlide === totalSlides - 1;
        }

        function changeSlide(direction) {
            showSlide(currentSlide + direction);
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') changeSlide(-1);
            if (e.key === 'ArrowRight') changeSlide(1);
        });

        showSlide(0);
    </script>
</body>
</html>
"""

# Display the HTML presentation
st.components.v1.html(html_content, height=800, scrolling=False)

# Add footer with instructions
st.markdown("---")
st.markdown("""
### 🎮 Navigation Instructions
- Use the **Previous** and **Next** buttons to navigate through slides
- Or use **Arrow Keys** (← →) on your keyboard
- Press **F11** for fullscreen mode in your browser

### 📊 Presentation Overview
This presentation covers:
- **9 comprehensive slides** about Transformer Models
- Decoder Models (GPT), Encoder Models (BERT), and Encoder-Decoder architectures
- Three hands-on lab overviews
- Complete with blue and yellow color theme
""")