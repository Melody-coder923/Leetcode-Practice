class Codec:
    def encode(self, strs: List[str]) -> str:
        return "😁".join(strs)
        

    def decode(self, s: str) -> List[str]:
        return s.split("😁")
        