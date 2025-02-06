import g4f, g4f.Provider

class LargeLanguageModel:
    def ResponseFromAI(self, prompt):
        self.user_query: list[dict[str, str]] = [{f"role": f"user", f"content": prompt}]
        
        self.response: str = g4f.ChatCompletion.create(model=f"gpt-4o-mini" , provider=g4f.Provider.DDG, messages=self.user_query)

        return self.response