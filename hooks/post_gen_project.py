#!/usr/bin/env python3
"""
Post-generation hook for React Native Cookiecutter Template.

This script runs after the cookiecutter template has been generated
to perform initial setup and provide guidance to the user.
"""

import os
import sys
import subprocess
import platform
from pathlib import Path


def run_command(command, cwd=None, shell=False):
    """Run a command and return success status."""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            shell=shell,
            check=True,
            capture_output=True,
            text=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr
    except FileNotFoundError:
        return False, f"Command not found: {command[0] if isinstance(command, list) else command}"


def check_requirements():
    """Check if required tools are installed."""
    print("🔍 Checking requirements...")
    
    requirements = {
        'node': ['node', '--version'],
        'npm': ['npm', '--version'],
    }
    
    missing = []
    for tool, cmd in requirements.items():
        success, output = run_command(cmd)
        if success:
            version = output.strip()
            print(f"  ✅ {tool}: {version}")
        else:
            print(f"  ❌ {tool}: Not found")
            missing.append(tool)
    
    if platform.system() == 'Darwin':  # macOS
        ios_requirements = {
            'xcode-select': ['xcode-select', '--version'],
            'pod': ['pod', '--version']
        }
        
        for tool, cmd in ios_requirements.items():
            success, output = run_command(cmd)
            if success:
                version = output.strip().split('\n')[0]
                print(f"  ✅ {tool}: {version}")
            else:
                print(f"  ⚠️  {tool}: Not found (required for iOS/macOS development)")
    
    return missing


def install_dependencies():
    """Install npm dependencies."""
    print("\n📦 Installing Node.js dependencies...")
    
    success, output = run_command(['npm', 'install'])
    if success:
        print("  ✅ npm install completed successfully")
        return True
    else:
        print(f"  ❌ npm install failed: {output}")
        return False


def install_ios_dependencies():
    """Install iOS/macOS dependencies if on macOS."""
    if platform.system() != 'Darwin':
        return True
    
    print("\n🍎 Installing iOS dependencies...")
    
    ios_path = Path('ios')
    if ios_path.exists():
        success, output = run_command(['pod', 'install'], cwd=ios_path)
        if success:
            print("  ✅ iOS pod install completed successfully")
        else:
            print(f"  ⚠️  iOS pod install failed: {output}")
            print("  💡 You can run 'cd ios && pod install' manually later")
    
    # Install macOS dependencies
    macos_path = Path('macos')
    if macos_path.exists():
        print("\n🖥️  Installing macOS dependencies...")
        success, output = run_command(['pod', 'install'], cwd=macos_path)
        if success:
            print("  ✅ macOS pod install completed successfully")
        else:
            print(f"  ⚠️  macOS pod install failed: {output}")
            print("  💡 You can run 'cd macos && pod install' manually later")
    
    return True


def create_src_directory():
    """Create src directory for organized code structure."""
    src_path = Path('src')
    if not src_path.exists():
        src_path.mkdir()
        print("📁 Created src/ directory for your application code")
        
        # Create some basic subdirectories
        subdirs = ['components', 'screens', 'utils', 'types']
        for subdir in subdirs:
            (src_path / subdir).mkdir()
            # Create index.ts files
            (src_path / subdir / 'index.ts').write_text(f'// Export your {subdir} from this file\n')
        
        print(f"  ✅ Created subdirectories: {', '.join(subdirs)}")


def cleanup_template_files():
    """Clean up any template-specific files that shouldn't be in the final project."""
    print("\n🧹 Cleaning up template files...")
    
    # Remove any .history directories that might have been created
    history_dirs = list(Path('.').glob('**/.history'))
    for history_dir in history_dirs:
        if history_dir.is_dir():
            import shutil
            shutil.rmtree(history_dir)
            print(f"  🗑️  Removed: {history_dir}")
    
    print("  ✅ Cleanup completed")


def display_success_message():
    """Display success message with next steps."""
    project_name = "{{cookiecutter.project_name}}"
    display_name = "{{cookiecutter.display_name}}"
    
    print(f"""
🎉 SUCCESS! Your React Native project '{display_name}' has been generated!

📁 Project Location: {os.getcwd()}

🚀 Next Steps:
   1. Start the Metro bundler:
      npm start

   2. Run your app on different platforms:
      • iOS:     npm run ios
      • Android: npm run android
      • macOS:   npm run macos

🧪 Development Commands:
   • Test:    npm test
   • Lint:    npm run lint
   • Type check: npx tsc --noEmit

📝 Useful Files:
   • App.tsx              - Main app component
   • src/                 - Your application code
   • package.json         - Dependencies and scripts
   • README.md            - Project documentation

💡 Tips:
   • Use NativeWind classes for styling (e.g., className="bg-blue-500 p-4")
   • Add platform-specific code with .ios.tsx, .android.tsx, .macos.tsx extensions
   • Check README.md for detailed setup and usage instructions

🆘 Need Help?
   • Run 'npx react-native doctor' to check your environment
   • Check the README.md for troubleshooting guides
   • Visit https://reactnative.dev for documentation

Happy coding! 🚀
""")


def main():
    """Main hook execution."""
    print("🔧 Setting up your React Native project...")
    print("=" * 60)
    
    try:
        # Check requirements
        missing = check_requirements()
        
        # Install dependencies
        if not missing or 'npm' not in missing:
            npm_success = install_dependencies()
            
            # Install platform-specific dependencies
            if npm_success:
                install_ios_dependencies()
        
        # Create organized directory structure
        create_src_directory()
        
        # Clean up template files
        cleanup_template_files()
        
        # Display success message
        display_success_message()
        
    except KeyboardInterrupt:
        print("\n\n❌ Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Setup failed with error: {e}")
        print("💡 You can complete the setup manually by running:")
        print("   npm install")
        if platform.system() == 'Darwin':
            print("   cd ios && pod install && cd ..")
            print("   cd macos && pod install && cd ..")
        sys.exit(1)


if __name__ == '__main__':
    main()