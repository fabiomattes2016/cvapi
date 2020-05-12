Funcionalidade: Endpoint de validação do Json
    @invalido
    Cenário: Json inválido
        Quando enviar o Json
            """
            {"Nome": "Fábio"}
            """
        Então a API deve retornar 400
    
    @valido
    Cenário: Json válido
        Quando enviar o Json
            """
            {
                "name": "George the Martian",
                "profession": "Youtube senior analyst",
                "phone": "+55 287298121",
                "email": "George@martian.com",
                "address": "73 N. Oak Drive - Dyersburg, TN 38024",
                "portfolio": "github.com/g_martian",
                "education": [
                    [
                        "PhD in the streets - Harvard",
                        "2001",
                        "phd in doing absolutelly nothing 24/7"
                    ]
                ],
                "experience": [
                    [
                        "Garbage collector",
                        "Jan 2000 - Mai 2003",
                        "Collecting garbage in other codes"
                    ]
                ],
                "skills": [
                    ["Python", 5],
                    ["JS", 1],
                    ["CSS", 2],
                    ["HTML", 1],
                    ["Cooking", 3]
                ],
                "languages": [
                    ["English", "Basic"],
                    ["Pirate English", "Native"]
                ]
            }
            """
        Então a API deve retornar 201