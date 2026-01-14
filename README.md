# STEPWISE 🟣  
### *Taking life one step at a time.*

STEPWISE is a **cognitive execution assistant** designed to support **neurodiverse children** (ADHD, autism spectrum, learning differences, executive dysfunction challenges) in completing everyday routines with confidence.

Instead of overwhelming children with long instructions, STEPWISE breaks tasks into **simple steps**, tracks progress step-by-step, and provides **gentle voice encouragement only when the child is stuck**.

---

##  Why STEPWISE?
Many children know *what* they need to do, but struggle with:
- remembering steps in the correct order  
- switching between tasks (task shifting)  
- staying focused without stress  
- executive functioning + time management  

STEPWISE reduces cognitive load by giving:
one step at a time  
a calm interface  
optional voice support only when needed  
simple Parent Setup + quick Child Mode execution  

---

## Key Features
###  Parent Mode (Routine Setup)
- Create routines like *“Get Ready for School”*, *“Morning Routine”*, *“Homework Time”*
- Add steps one-by-one
- Save the routine and send it to Child Mode instantly (no database required)

###  Child Mode (Execution Assistant)
- Shows one step clearly on screen
- Child presses **DONE** to move to the next step
- If the child is stuck, STEPWISE automatically provides:
  - a supportive help message  
  - **voice guidance using Azure Speech AI**

### Parent Insights Mode
- Displays insights based on how long each step took
- Uses **Azure AI Language (Text Analytics)** to extract key phrases and summarize delays

---

##  AI Services Used (Microsoft Azure)
 **Azure AI Speech**  
- Generates natural, friendly voice guidance when the child is stuck  
- Voice Example: `en-US-JennyNeural`  
- Region: `koreacentral`

 **Azure AI Language (Text Analytics)**  
- Generates parent insights from routine execution logs  
- Example: identifies which steps took longer

---

##  Tech Stack
### Frontend
- HTML + CSS + JavaScript  
- Responsive purple UI (Parent / Child / Insights)

### Backend
- Python + FastAPI  
- In-memory execution engine (no DB needed)

### Cloud / AI
- Azure AI Speech  
- Azure AI Language

---

## 📁 Project Structure
