import asyncio
from environment_setup import validate_environment
from src.utils.runners import create_sections, class_agent


async def sections():
    await create_sections()

async def agent(prompt: str):
    return await class_agent(prompt)


async def main():
    # Validate environment
    success = validate_environment()
    if not success:
        return

    # Create sections
    await sections()
    print('Sections created successfully')
    print('==' * 40)
    print("Welcome to PC Agent CLI (Ctrl + C to exit)")
    print('==' * 40)

    # Chat loop
    while True:
        prompt = input("Enter the prompt: ")
        answer = await agent(prompt)
        print(f"[PC Agent]: {answer}")


if __name__ == "__main__":
    asyncio.run(main())
