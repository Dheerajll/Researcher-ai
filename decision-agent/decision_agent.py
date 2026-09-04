#!/usr/bin/env python3
"""
Decision Agent - AI-powered decision making assistant

This agent helps you make decisions by:
1. Finding the best options for your criteria
2. Comparing what actually matters (key differentiators)
3. Removing useless information (noise reduction)
4. Giving one clear recommendation
5. Explicitly stating uncertainties instead of guessing

Usage:
    python decision_agent.py "Your decision question here"
    
Example:
    python decision_agent.py "Which laptop should I buy for software development under $2000?"
"""

import sys
import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class Option:
    """Represents a single option being considered"""
    name: str
    description: str
    pros: List[str] = field(default_factory=list)
    cons: List[str] = field(default_factory=list)
    key_features: Dict[str, Any] = field(default_factory=dict)
    confidence: float = 1.0  # How confident we are in this information
    uncertainties: List[str] = field(default_factory=list)


@dataclass
class ComparisonCriteria:
    """Criteria that actually matter for the decision"""
    name: str
    weight: float  # Importance weight (0-1)
    description: str


@dataclass
class DecisionResult:
    """The final decision output"""
    question: str
    options_considered: List[Option]
    criteria_used: List[ComparisonCriteria]
    recommendation: Option
    reasoning: str
    key_differentiators: List[str]
    information_discarded: List[str]
    uncertainties: List[str]
    confidence_level: str
    
    def to_formatted_string(self) -> str:
        """Return a nicely formatted string representation"""
        output = []
        output.append("=" * 70)
        output.append("DECISION AGENT RECOMMENDATION")
        output.append("=" * 70)
        output.append(f"\n📋 YOUR QUESTION:\n{self.question}\n")
        
        output.append(f"\n🎯 MY RECOMMENDATION:\n**{self.recommendation.name}**\n")
        output.append(f"{self.recommendation.description}\n")
        
        output.append(f"\n💡 KEY REASONING:\n{self.reasoning}\n")
        
        output.append(f"\n⚖️ WHAT ACTUALLY MATTERED (Key Differentiators):")
        for i, diff in enumerate(self.key_differentiators, 1):
            output.append(f"  {i}. {diff}")
        
        output.append(f"\n🗑️ INFORMATION DISCARDED (Not Useful):")
        for info in self.information_discarded:
            output.append(f"  • {info}")
        
        if self.uncertainties:
            output.append(f"\n⚠️ UNCERTAINTIES (I'm not guessing on these):")
            for unc in self.uncertainties:
                output.append(f"  ⚠️ {unc}")
        
        output.append(f"\n📊 CONFIDENCE LEVEL: {self.confidence_level}")
        
        output.append(f"\n📝 OPTIONS CONSIDERED:")
        for opt in self.options_considered:
            status = "✅ RECOMMENDED" if opt == self.recommendation else "○"
            output.append(f"\n  {status} {opt.name}")
            if opt.pros:
                output.append(f"     Pros: {', '.join(opt.pros[:3])}")
            if opt.cons:
                output.append(f"     Cons: {', '.join(opt.cons[:3])}")
            if opt.uncertainties:
                output.append(f"     Uncertainties: {', '.join(opt.uncertainties)}")
        
        output.append("\n" + "=" * 70)
        return "\n".join(output)


class DecisionAgent:
    """
    AI Agent for making clear, well-reasoned decisions
    
    This agent follows a structured approach:
    1. Parse the decision request
    2. Identify relevant options
    3. Determine what criteria actually matter
    4. Filter out noise and irrelevant information
    5. Compare options on key differentiators
    6. Make a clear recommendation with stated uncertainties
    """
    
    def __init__(self):
        self.verbose = False
    
    def analyze_decision(self, question: str, context: Optional[Dict] = None) -> DecisionResult:
        """
        Analyze a decision request and provide a recommendation
        
        Args:
            question: The decision question to answer
            context: Optional context about user preferences, constraints, etc.
        
        Returns:
            DecisionResult with recommendation and reasoning
        """
        
        # For demonstration, we'll use a rule-based approach
        # In production, this would integrate with LLM APIs or domain-specific data sources
        
        # Step 1: Categorize the decision type
        decision_type = self._categorize_decision(question)
        
        # Step 2: Generate relevant options based on decision type
        options = self._generate_options(decision_type, question, context)
        
        # Step 3: Identify what criteria actually matter
        criteria = self._identify_criteria(decision_type, context)
        
        # Step 4: Evaluate options against criteria
        evaluated_options = self._evaluate_options(options, criteria, context)
        
        # Step 5: Identify key differentiators
        differentiators = self._find_differentiators(evaluated_options, criteria)
        
        # Step 6: Identify information to discard (noise)
        discarded_info = self._identify_noise(decision_type, question)
        
        # Step 7: Select best option
        best_option = self._select_best_option(evaluated_options, criteria)
        
        # Step 8: Compile uncertainties
        uncertainties = self._compile_uncertainties(evaluated_options)
        
        # Step 9: Generate reasoning
        reasoning = self._generate_reasoning(best_option, criteria, differentiators)
        
        # Step 10: Determine confidence level
        confidence_level = self._determine_confidence(uncertainties, evaluated_options)
        
        return DecisionResult(
            question=question,
            options_considered=evaluated_options,
            criteria_used=criteria,
            recommendation=best_option,
            reasoning=reasoning,
            key_differentiators=differentiators,
            information_discarded=discarded_info,
            uncertainties=uncertainties,
            confidence_level=confidence_level
        )
    
    def _categorize_decision(self, question: str) -> str:
        """Categorize the type of decision being made"""
        question_lower = question.lower()
        
        categories = {
            'tech_purchase': ['laptop', 'phone', 'computer', 'tablet', 'headphones', 'monitor', 'keyboard', 'mouse'],
            'software_service': ['software', 'app', 'service', 'platform', 'tool', 'saas'],
            'learning': ['learn', 'course', 'book', 'tutorial', 'skill'],
            'career': ['job', 'career', 'role', 'position'],
            'investment': ['invest', 'stock', 'fund', 'crypto'],
            'travel': ['travel', 'vacation', 'hotel', 'flight', 'destination'],
            'health': ['diet', 'exercise', 'workout', 'supplement'],
            'home': ['appliance', 'furniture', 'home'],
        }
        
        for category, keywords in categories.items():
            if any(keyword in question_lower for keyword in keywords):
                return category
        
        return 'general'
    
    def _generate_options(self, decision_type: str, question: str, context: Optional[Dict]) -> List[Option]:
        """Generate relevant options based on decision type"""
        
        # Sample option databases (in production, these would be more comprehensive)
        tech_options = {
            'laptop': [
                Option(
                    name="MacBook Pro 14-inch (M3)",
                    description="Premium laptop with excellent performance and battery life",
                    pros=["Exceptional performance", "Great battery life", "Excellent display", "Premium build"],
                    cons=["Expensive", "Limited ports", "Not upgradeable"],
                    key_features={"price": 1999, "battery": "17 hours", "weight": "3.5 lbs"},
                ),
                Option(
                    name="Dell XPS 15",
                    description="Windows alternative with great display and performance",
                    pros=["Beautiful display", "Good performance", "More ports than MacBook"],
                    cons=["Battery life varies", "Can run hot", "Heavier"],
                    key_features={"price": 1799, "battery": "10 hours", "weight": "4.2 lbs"},
                ),
                Option(
                    name="Framework Laptop 13",
                    description="Fully repairable and upgradeable laptop",
                    pros=["Fully repairable", "Upgradeable", "Good port selection", "Ethical choice"],
                    cons=["Performance slightly lower", "Less premium feel"],
                    key_features={"price": 1399, "battery": "10 hours", "weight": "2.9 lbs"},
                ),
            ],
            'phone': [
                Option(
                    name="iPhone 15 Pro",
                    description="Premium smartphone with best-in-class ecosystem",
                    pros=["Excellent camera", "Long support", "Premium build", "Best ecosystem"],
                    cons=["Expensive", "Less customizable", "Lightning/USB-C transition"],
                ),
                Option(
                    name="Samsung Galaxy S24 Ultra",
                    description="Feature-rich Android flagship",
                    pros=["Amazing display", "S Pen included", "Versatile cameras", "Highly customizable"],
                    cons=["Expensive", "Large size", "Learning curve"],
                ),
            ],
        }
        
        software_options = {
            'project_management': [
                Option(
                    name="Linear",
                    description="Fast, opinionated project management for software teams",
                    pros=["Incredibly fast", "Great UX", "Developer-focused"],
                    cons=["Less flexible", "Pricier per seat"],
                ),
                Option(
                    name="Notion",
                    description="All-in-one workspace with maximum flexibility",
                    pros=["Extremely flexible", "Good for documentation", "Affordable"],
                    cons=["Can be slow", "Steeper learning curve", "Too much freedom"],
                ),
            ],
        }
        
        # Return appropriate options based on type
        if decision_type == 'tech_purchase':
            for key in tech_options:
                if key in question.lower():
                    return tech_options[key][:3]  # Limit to top 3
            return tech_options.get('laptop', [])[:2]
        
        elif decision_type == 'software_service':
            for key in software_options:
                if any(k in question.lower() for k in ['project', 'task', 'manage']):
                    return software_options['project_management']
            return []
        
        # Default fallback options for general decisions
        return [
            Option(name="Option A", description="First viable option", pros=[], cons=[]),
            Option(name="Option B", description="Second viable option", pros=[], cons=[]),
        ]
    
    def _identify_criteria(self, decision_type: str, context: Optional[Dict]) -> List[ComparisonCriteria]:
        """Identify what criteria actually matter for this decision"""
        
        base_criteria = {
            'tech_purchase': [
                ComparisonCriteria("performance", 0.25, "How well it performs core tasks"),
                ComparisonCriteria("value", 0.20, "Price relative to features and quality"),
                ComparisonCriteria("reliability", 0.20, "Build quality and longevity"),
                ComparisonCriteria("ecosystem", 0.15, "Integration with your existing tools"),
                ComparisonCriteria("support", 0.10, "Customer service and warranty"),
                ComparisonCriteria("resale_value", 0.10, "Value retention over time"),
            ],
            'software_service': [
                ComparisonCriteria("usability", 0.25, "How easy and pleasant to use"),
                ComparisonCriteria("features", 0.20, "Does it have what you need"),
                ComparisonCriteria("pricing", 0.20, "Cost effectiveness"),
                ComparisonCriteria("integration", 0.15, "Works with your stack"),
                ComparisonCriteria("scalability", 0.10, "Grows with your needs"),
                ComparisonCriteria("support", 0.10, "Help when you need it"),
            ],
            'general': [
                ComparisonCriteria("effectiveness", 0.30, "Does it solve your problem"),
                ComparisonCriteria("cost", 0.25, "Total cost of ownership"),
                ComparisonCriteria("ease_of_use", 0.20, "How easy to adopt"),
                ComparisonCriteria("longevity", 0.15, "How long it will serve you"),
                ComparisonCriteria("risk", 0.10, "What could go wrong"),
            ],
        }
        
        return base_criteria.get(decision_type, base_criteria['general'])
    
    def _evaluate_options(self, options: List[Option], criteria: List[ComparisonCriteria], 
                         context: Optional[Dict]) -> List[Option]:
        """Evaluate each option against the criteria"""
        # In a full implementation, this would score each option
        # For now, we enhance options with evaluation metadata
        for option in options:
            # Add scoring placeholder
            option.key_features['overall_score'] = 0.0  # Would be calculated
        return options
    
    def _find_differentiators(self, options: List[Option], 
                             criteria: List[ComparisonCriteria]) -> List[str]:
        """Find the key factors that differentiate the options"""
        differentiators = []
        
        if len(options) < 2:
            return ["Only one viable option identified"]
        
        # Find meaningful differences
        if options[0].pros and options[1].pros:
            differentiators.append(f"{options[0].name}: {options[0].pros[0]}")
            differentiators.append(f"{options[1].name}: {options[1].pros[0]}")
        
        if options[0].cons and options[1].cons:
            differentiators.append(f"Trade-off: {options[0].cons[0]} vs {options[1].cons[0]}")
        
        return differentiators[:5]  # Limit to top 5
    
    def _identify_noise(self, decision_type: str, question: str) -> List[str]:
        """Identify common noise/information that should be ignored"""
        
        noise_patterns = {
            'tech_purchase': [
                "Marketing buzzwords (AI-powered, revolutionary, etc.)",
                "Minor spec differences that don't impact real usage",
                "Brand loyalty arguments without substance",
                "Outdated reviews (>1 year old for fast-moving tech)",
                "Edge case scenarios unlikely to affect you",
            ],
            'software_service': [
                "Feature count without quality assessment",
                "Hype from recent funding announcements",
                "Comparisons to tools you're not using",
                "Enterprise features you won't need",
            ],
            'general': [
                "Opinions without reasoning",
                "Outdated information",
                "Edge cases that don't apply to your situation",
                "Status signaling over substance",
            ],
        }
        
        return noise_patterns.get(decision_type, noise_patterns['general'])[:4]
    
    def _select_best_option(self, options: List[Option], 
                           criteria: List[ComparisonCriteria]) -> Option:
        """Select the best option based on criteria"""
        if not options:
            return Option(name="No Recommendation", description="Insufficient data")
        
        # Simple selection logic (would be more sophisticated in production)
        # Prioritize options with fewer cons and more relevant pros
        scored_options = []
        for opt in options:
            score = len(opt.pros) - (len(opt.cons) * 0.5)
            scored_options.append((score, opt))
        
        scored_options.sort(reverse=True, key=lambda x: x[0])
        return scored_options[0][1]
    
    def _compile_uncertainties(self, options: List[Option]) -> List[str]:
        """Compile all uncertainties from the analysis"""
        uncertainties = []
        
        for opt in options:
            uncertainties.extend([f"[{opt.name}] {u}" for u in opt.uncertainties])
        
        # Add general uncertainties
        uncertainties.append("Individual experiences may vary based on specific use case")
        uncertainties.append("Prices and availability change frequently")
        
        return uncertainties
    
    def _generate_reasoning(self, recommendation: Option, criteria: List[ComparisonCriteria],
                           differentiators: List[str]) -> str:
        """Generate clear reasoning for the recommendation"""
        reasoning_parts = [
            f"We recommend {recommendation.name} because:",
            "",
        ]
        
        # Add top reasons
        for i, pro in enumerate(recommendation.pros[:3], 1):
            reasoning_parts.append(f"{i}. {pro}")
        
        if recommendation.cons:
            reasoning_parts.append("")
            reasoning_parts.append(f"Trade-off to accept: {recommendation.cons[0]}")
        
        return "\n".join(reasoning_parts)
    
    def _determine_confidence(self, uncertainties: List[str], 
                             options: List[Option]) -> str:
        """Determine overall confidence level"""
        if len(uncertainties) > 5:
            return "MODERATE - Several uncertainties to consider"
        elif len(uncertainties) > 2:
            return "HIGH - Minor uncertainties noted above"
        else:
            return "VERY HIGH - Clear recommendation with minimal uncertainty"


def main():
    """Main entry point for the decision agent"""
    
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n❌ ERROR: Please provide a decision question")
        print("\nExample usage:")
        print('  python decision_agent.py "Which laptop should I buy for software development under $2000?"')
        sys.exit(1)
    
    # Get the decision question from command line
    question = " ".join(sys.argv[1:])
    
    # Initialize the agent
    agent = DecisionAgent()
    
    print(f"\n🤔 Analyzing your decision: \"{question}\"")
    print("   (This analyzes options, filters noise, and finds what matters...)\n")
    
    # Get the decision result
    result = agent.analyze_decision(question)
    
    # Print the formatted result
    print(result.to_formatted_string())
    
    # Optionally save to file
    save_file = "decision_result.txt"
    with open(save_file, "w") as f:
        f.write(result.to_formatted_string())
    print(f"\n💾 Saved to {save_file}")


if __name__ == "__main__":
    main()
