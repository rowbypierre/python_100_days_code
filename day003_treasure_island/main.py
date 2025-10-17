import os
import time


def clear_screen():
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause(seconds):
    """Create delay in terminal screen for provided number of seconds (float)."""
    time.sleep(seconds)


def prompt_parser(prompt):
    """Format and print game prompt (str) for readability."""
    counter = 0
    clean_prompt = map(lambda x: x.strip(), prompt.split(","))
    for line in clean_prompt:
        counter += 1
        if line.count("OR") != 0:
            print("\n" + line + "\n")
        elif line.count(":") != 0:
            print(line + "\n")
        else:
            print(line)


if __name__ == "__main__":
    print(
        """
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@88000GCCGGCGG0088@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@80GCftt1;:::,...  .  .,,,:::;i1tLCG08@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@0GCf;.                                   .;tCG08@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@0C1:..            .,,;i1tfLfft1ii;,..             .:if08@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@Gt;.            .:ifG088@@@@@@@@@@@@@@800L1:.       ..    ,iL0@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@8f:.   . .      .iLG8@@@@@@@@@@@@@@@@@@@@@@@@@@0C1,    .i:      :iL8@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@Ci.     ..     .iL0@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@8Ct,  ..    .  .,,1G@@@@@@@@@@@@@@
    @@@@@@@@@@@@L;.    .  ..   .iG@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@0f:          .  ;tC@@@@@@@@@@@@
    @@@@@@@@@@Gi       .   . :t0@@@@@@@@@@@@GLf1;:,....,,,:;tfC0@@@@@@@@@@@8f,          .. .10@@@@@@@@@@
    @@@@@@@@01.             iC@@@@@@@@@@@0f;.                  ,1G@@@@@@@@@@@81          .,. ,L@@@@@@@@@
    @@@@@@@C,             .18@@@@@@@@@@8L:           ..          .18@@@@@@@@@@@C,        ..    ;0@@@@@@@
    @@@@@8f.        .    ,f@@@@@@@@@@@0i         ..  ..       .    ;8@@@@@@@@@@@C:              :G@@@@@@
    @@@@@t.             .f@@@@@@@@@@@8f     .    ,.          .  ..  t8@@@@@@@@@@@C;  ..          :C@@@@@
    @@@81..            .C@@@@@@@@@@@@L,               ..    .   ..  ;G@@@@@@@@@@@@L        .      i8@@@@
    @@8f  .     .     .1@@@@@@@@@@@@@1                          .   .C@@@@@@@@@@@@8L  .            ;0@@@
    @@C. ..           :G@@@@@@@@@@@@@1    .;1tt1:. .     ,1ttt1:.   :G@@@@@@@@@@@@@8;    ..        .f8@@
    @8t        .      i@@@@@@@@@@@@@@L,  iG@@@@@@Gi .. ,L8@@@@@8L,  i0@@@@@@@@@@@@@8L,.:  ..        ,C@@
    @f..       .     ;C@@@@@@@@@@@@@@8f  L@@@@@@@@f    :@@@@@@@@@i .L8@@@@@@@@@@@@@@0:.:        ...  f@@
    @1               t8@@@@@@@@@@@@@@@G. C@@@@@@0t, ,;, tG@@@@@@@i ;@@@@@@@@@@@@@@@@@; ,,.      ..   ;G@
    0i               f@@@@@@@@@@@@@@8f:  :tGGL1;. ,f0@C: .;ifCCti, .iG@@@@@@@@@@@@@@@i ,,. .     ..  ,L@
    0;           .. .L@@@@@@@@@@@@@@0;            t@@@@0,,,          L@@@@@@@@@@@@@@@t,. ..           t@
    0i              ,C@@@@@@@@@@@@@@@8GLLf;   ..  ;t11ti. .:.  .ifLLG8@@@@@@@@@@@@@@@L,  .          . t@
    0;              ,C@@@@@@@@@@@@@@@@@@@@@0i..,           .,iL8@@@@@@@@@@88@@@@@@@@@f,    .     ..  .L@
    0;              ,C@@@@@@@@@0LG88@@@@8@@@@1:;  . .      ,f8@@@@@@@880CG88@@@@@@@@@C:              ,L@
    8i     .        ,C@@@@@@@@@@8GCCCLL0@@@@@088fG0f0LLGfC0G8@@@@8CC0CC08@@@@@@@@@@@@L,              :C@
    @1              .L@@@@@@@@@@@@@@8Cfti1LG8@@@@@@@@@@@@@@@80Cfi1fL8@@@@@@@@@@@@@@@@f,         ..   18@
    @t..      .,     f@@@@@@@@@@@@@@@@@G:   .C@@@@@@@@@@@@@@i.  .:t8@@@@@@@@@@@@@@@@@t.     ..  ..   L@@
    @81 ..           t8@@@@@@@@@@@@@@@@88Gf;,;1CG8@@@@@@8GLi;:1C08@@@@@@@@@@@@@@@@@@@i .    .   .   :G@@
    @@C...           :C@@@@@@@@@@@@@@@@@@@@@80Lii;itLCt;iif008@@@@@@@@@@@@@@@@@@@@@@8; .           .f8@@
    @@8f              i@@@@@@@@@@@@@@@@@@@@@@@@8f;.     ;L88@@@@@@@@@@@@@@@@@@@@@@@@L,            .i8@@@
    @@@8;             :G@@@@@@@@@@@@@@@@@@80Li::;fG8@@8GGC1.:1fG8@@@@@@@@@@@@@@@@@@8i.      .     1@@@@@
    @@@@81            .t@@@@@@@@@@@@@@8Cti:  :L8@@@@@@@@@@8C;   ,itL8@@@@@@@@@@@@@@L.            iG@@@@@
    @@@@@8t          . .f8@@@@@@@@@@@@@L: .ifC8@@@@@@@@@@@@@Gf1;,,18@@@@@@@@@@@@@@L             10@@@@@@
    @@@@@@8L,            t8@@@@@@@@80LfLfL0@@@@@@@@@@@@@@@@@@@@@8LfLfL08@@@@@@@@@L,      ..   ,f8@@@@@@@
    @@@@@@@@0i.       .. .10@@@@000CLG8@@@@@@@@@@@@@@@@@@@@@@@@@@@@88LfC008@@@@@t,       ..  ;G@@@@@@@@@
    @@@@@@@@@@C;        .  :C@@0088@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@8008@@C;     ..    ,L8@@@@@@@@@@
    @@@@@@@@@@@@L;.          10@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@8Ci.   ..     ,t8@@@@@@@@@@@@
    @@@@@@@@@@@@@@Ci.         .iC8@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@8f:     .    .;L8@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@8f;.     .   ,1C0@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@0f;.   ..    .;fG@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@0C1:.        ,;if8@@@@@@@@@@@@@@@@@@@@@@@@@0fi:.         .;fG8@@@@@@@@@@@@@@@@008
    08@@@@@@@@@@@@@@@@@@@@8GLti:        ;G@@@@@@@@@@@@@@@@@@@@@@@@L        ,;itC0@@@@@@@@@@@@@@@@@@@@tf@
    GLG@@@@@@@@@@@@@@@@@@@@@@@@@GLf1. .  C@@@@@@@@@@@@@@@@@@@@@@@@f  . .tCC8@@@@@@@@@@@@@@@@@@@@@@@@0,i@
    G;:G@@@@@@@@@@@@@@@@@@@@@@@@@@@8, . .C@@@@@@@@@@@@@@@@@@@@@@@81  . ;@@@@@@@@@@@@@@@@@@@@@@@@@@0L: 1@
    0i .;tLG00888888880888888888008G.    L@@@@@@@@@@@@@@@@@@@@@@@81   .1GGGGGGGGGGGGGGGGGCCCCCLLt;,   1@
    8i       ...  ...               .    f@@@@@@@@@@@@@@@@@@@@@@@01       ...                         1@
    8i .                            .    18@@@@@@@@@@@@@@@@@@@@@@01    .:. .                          1@
    81          .                        10@@@@@@@@@@@@@@@@@@@@@@L:    .,...         ...              i8
    @1 .        .       ..       ..      i0@@@@@@@@@@@@@@@@@@@@@@;    .   ....       ..               i8
    @1                  .                ;G@@@@@@@@@@@@@@@@@@@@@@i                                    i8
    @f,:::::::::::;::::::::::::;::;;;;;::1G@@@@@@@@@@@@@@@@@@@@@@t:;i1t1ttt1111t1tt1ttttttttttttttttttC@""",
        "\nWelcome to the Once in a Lifttime Adventure. \nGoodluck!",
    )
    pause(5)
    clear_screen()

    prompts = [
        """You start at a familiar crossroads but this time., 
            The journey unfolds quite differently., 
            You turn left and shortly encounter a wise old traveler., 
            He offers you a choice:, 
            1. To take a lantern and venture into the dark forest., 
            OR, 
            2. A shovel to dig near the ancient oak tree.""",
        """Choosing the lantern you head into the forest., 
            There you find a hidden grove with three statues., 
            Each statue has a riddle., 
            With no time to think - which riddle do you solve:, 
            1. The eagle, 
            OR, 
            2. The lion, 
            OR, 
            3. The dolphin""",
        """By solving the eagle's riddle do you receive a silver key., 
            With key in hand - you journey on to a castle shrouded in mist.,
            The castle has three towers - each locked.,
            Which tower do you unlock:, 
            1. Tower of Whispers, 
            OR, 
            2. Tower of Secrets, 
            OR, 
            3. Tower of the Unknown""",
        """Inside - you climb the spiral staircase to find a room with two doors., 
            Which door do you enter:, 
            1. The one guarded by a knight,
            OR,
            2. The other by a bishop""",
        """ The knight allows you through his door - leading to a garden labyrinth., 
            At the heart of the labyrinth - you discover a well., 
            The well is actually a portal to a subterranean cave where the treasure is said to be guarded by a dragon.,
            You must choose between three tunnels:,
            1. Tunnel filled with a faint glow,
            OR,
            2. Tunnel with sound of running water,
            OR,
            3. Tunnel with no sound""",
        """ Choosing the tunnel with the glow - you find the dragon asleep.,
            The treasure is within reach.,
            You must choose between:,
            1. Taking the treasure and running fast.,
            OR,
            2. Carefully extracting the treasure without waking the dragon.,
            OR,
            3. Silently leaving and returning back a weapon capable of slaying the dragon.""",
    ]

    prompt_num = 0
    input_count = 0
    input_limit = 6
    choices = {
        0: {"right": 1, "wrong": 2},
        1: {"right": 1, "wrong": [2, 3]},
        2: {"right": 1, "wrong": [2, 3]},
        3: {"right": 1, "wrong": 2},
        4: {"right": 1, "wrong": [2, 3]},
        5: {"right": 2, "wrong": [1, 3]},
    }

    def all_choices():
        """Return possible choices for game player as list."""
        return [
            numerals
            for choice in choices[prompt_num].values()
            for numerals in str(choice)
            if numerals.isalnum()
        ]

    game_on = True

    for prompt in prompts:
        prompt_parser(prompts[prompt_num])

        while game_on:
            limit_hit = input_count >= input_limit

            if not limit_hit:
                decision = input(f"\nEnter {all_choices()}: ").strip()
                valid_input = decision in all_choices()

            if limit_hit or valid_input:
                right_choice = int(decision) == choices[prompt_num]["right"]

                if (not right_choice) or limit_hit:
                    print("\nGame over. Hopefully you find the treasure next time.")
                    game_on = False
                    pause(2)
                    break
                elif right_choice:
                    print("\n!!!GREAT DECISION!!!")
                    counter = 0
                    prompt_num += 1
                    pause(2)
                    clear_screen()
                    break
            elif not valid_input:
                counter += 1
                print("Input invalid.")

                if counter == input_limit - 1:
                    print("Last attempt to input a valid input.")

        clear_screen()
        if not game_on:
            break
        elif prompt_num == max(list(choices.keys())) + 1:
            print("""\n!!!GREAT DECISION!!!\n
            \nYou carefully extract the treasure without waking the dragon.
            \nThis is done with a steady hand and a brave heart.
            \nYou exit through a hidden path that leads back to the surface.
            \nYour ship awaits to carry you and your newfound riches.""")
            pause(30)
            clear_screen()
