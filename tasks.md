# TASKS.md – SetuAI (Voice-First Multilingual AI for Bharat)

## 🎯 24-Hour Hackathon Goal

Build a production-ready MVP of SetuAI that:

- Accepts voice input in Hindi (extendable to 10+ languages)
- Uses Amazon Transcribe → AWS Bedrock (Claude 3.5 Sonnet)
- Implements RAG using OpenSearch
- Returns structured scheme guidance
- Converts output to voice using Amazon Polly
- Stores user session + profile in DynamoDB
- Uses S3 for scheme data + audio storage
- Fully serverless using AWS Lambda

---

# 🏗 Phase 1 – AWS Infrastructure Setup

## Task 1.1 – Create Core AWS Resources

- [ ] Create S3 bucket: `setuai-schemes-data`
- [ ] Create S3 bucket: `setuai-audio-storage`
- [ ] Create DynamoDB table: `SetuAI_UserProfiles`
- [ ] Create DynamoDB table: `SetuAI_ConversationContext`
- [ ] Enable Amazon Bedrock (Claude 3.5 Sonnet)
- [ ] Create OpenSearch Serverless collection
- [ ] Configure IAM roles for Lambda access
- [ ] Enable Amazon Transcribe
- [ ] Enable Amazon Polly

Success Criteria:
- Lambda can access S3, DynamoDB, Bedrock, Polly, Transcribe.

---

# 🧠 Phase 2 – Knowledge Base & RAG Setup

## Task 2.1 – Scheme Data Preparation

- [ ] Collect 20 central + state schemes
- [ ] Convert PDFs into structured JSON format
- [ ] Upload scheme JSON to S3
- [ ] Generate embeddings using Bedrock
- [ ] Store vectors in OpenSearch

Success Criteria:
- Query: "PM Awas Yojana eligibility"
- OpenSearch returns correct contextual documents

---

# 🎙 Phase 3 – Voice Processing Lambda

## Task 3.1 – Create Voice Lambda

Flow:
1. Receive audio
2. Upload to S3
3. Send to Amazon Transcribe
4. Detect language
5. Return transcript

Success Criteria:
- Audio <30 sec processed in <3 seconds
- ≥85% transcription accuracy (Requirement 1) :contentReference[oaicite:2]{index=2}

---

# 🤖 Phase 4 – AI Processing Lambda

## Task 4.1 – Implement RAG Flow

Flow:
1. Receive transcript
2. Fetch user profile (DynamoDB)
3. Query OpenSearch
4. Inject context into Claude 3.5 Sonnet prompt
5. Generate structured response

Prompt Structure:
- User Query
- Retrieved Scheme Context
- User Profile
- Output Format (Step-by-step guidance)

Success Criteria:
- Response matches latest scheme info (Requirement 4) :contentReference[oaicite:3]{index=3}
- Structured breakdown of eligibility & documents

---

# 🔊 Phase 5 – Voice Response Lambda

## Task 5.1 – Polly Integration

- [ ] Convert AI text → speech
- [ ] Optimize bitrate for low-bandwidth mode
- [ ] Store audio in S3
- [ ] Return streaming URL

Success Criteria:
- Natural regional pronunciation
- Supports interruption handling

---

# 📡 Phase 6 – Low Bandwidth Optimization

## Task 6.1 – Enable Low_Bandwidth_Mode

- [ ] Detect bandwidth <64kbps
- [ ] Compress audio by ≥70%
- [ ] Enable chunked streaming
- [ ] Cache frequent queries

Success Criteria:
- Basic query <100KB transfer (Requirement 3) :contentReference[oaicite:4]{index=4}

---

# 🔐 Phase 7 – Security & Guardrails

## Task 7.1 – Bedrock Guardrails

- [ ] Enable contextual grounding
- [ ] Block financial/legal advice
- [ ] Mask Aadhaar / PII
- [ ] Encrypt data at rest & transit

Success Criteria:
- No hallucinated scheme data
- PII auto-redacted

---

# 📊 Phase 8 – Performance & Scaling

## Task 8.1 – Load Testing

- [ ] Simulate 1,000 concurrent users
- [ ] Measure Lambda cold start times
- [ ] Optimize memory allocation

Target:
- 95% requests <5 seconds
- Supports 10,000 concurrent users (Requirement 9) :contentReference[oaicite:5]{index=5}

---

# 🧪 Phase 9 – Testing Strategy

## Unit Tests

- Voice accuracy tests
- OpenSearch retrieval tests
- DynamoDB CRUD tests

## Property-Based Tests

Tag Format:
Feature: setu-ai, Property {number}

Validate:
- Multilingual consistency
- Bandwidth compression
- Contextual grounding

(Aligned with Design Properties 1–13) :contentReference[oaicite:6]{index=6}

---

# 🏁 Final Demo Checklist

- [ ] User speaks in Hindi
- [ ] Transcription successful
- [ ] Relevant schemes retrieved
- [ ] Structured eligibility response generated
- [ ] Voice response returned
- [ ] Under 5 seconds total response time
- [ ] Works under simulated 2G bandwidth

---

# 🎖 Stretch Goals (If Time Permits)

- WhatsApp Integration
- Deadline notification system
- Proactive scheme recommendation
- Multi-language switching mid-conversation

---

# 🏆 Hackathon Winning Factors

- Real Bharat problem
- Voice-first for rural India
- Low-bandwidth resilience
- Fully serverless architecture
- Responsible AI with Guardrails
- Scalable to millions
