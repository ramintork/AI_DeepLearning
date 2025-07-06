#!/usr/bin/env python3
"""
Create a high-level system architecture diagram for Vibe Database Manager
Generates a PDF with comprehensive system architecture visualization
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

def create_architecture_diagram():
    """Create comprehensive system architecture diagram"""
    
    # Create figure with high DPI for PDF quality
    fig, ax = plt.subplots(1, 1, figsize=(16, 12), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Define colors
    colors = {
        'frontend': '#3498db',      # Blue
        'backend': '#e74c3c',       # Red
        'database': '#2ecc71',      # Green
        'ai': '#9b59b6',           # Purple
        'external': '#f39c12',      # Orange
        'connection': '#34495e'     # Dark gray
    }
    
    # Title
    ax.text(8, 11.5, 'Vibe Database Administration Assistant', 
            fontsize=20, fontweight='bold', ha='center')
    ax.text(8, 11, 'System Architecture Overview', 
            fontsize=14, ha='center', style='italic')
    
    # Frontend Layer (Top)
    frontend_box = FancyBboxPatch((1, 9), 14, 1.5, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor=colors['frontend'], 
                                  alpha=0.7, edgecolor='black')
    ax.add_patch(frontend_box)
    ax.text(8, 9.75, 'Frontend Layer', fontsize=14, fontweight='bold', ha='center', color='white')
    ax.text(3, 9.4, '• Bootstrap 5 UI\n• ChatGPT-style Interface', fontsize=10, ha='left', color='white')
    ax.text(8, 9.4, '• JavaScript Client\n• Real-time Chat', fontsize=10, ha='center', color='white')
    ax.text(13, 9.4, '• File Downloads\n• Table Views', fontsize=10, ha='right', color='white')
    
    # Backend Services Layer
    backend_box = FancyBboxPatch((1, 6.5), 14, 2, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor=colors['backend'], 
                                 alpha=0.7, edgecolor='black')
    ax.add_patch(backend_box)
    ax.text(8, 7.8, 'Backend Services Layer (Flask)', fontsize=14, fontweight='bold', ha='center', color='white')
    
    # Backend components with proper spacing to avoid overlap
    ax.text(2.5, 7.6, 'Route Handlers', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(2.5, 7.0, '• Main Routes\n• Auth Routes\n• Database Routes\n• AI Routes', fontsize=8, ha='center', color='white')
    
    ax.text(6, 7.6, 'Service Layer', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(6, 7.0, '• Database Manager\n• AI Services\n• Health Monitor\n• PostgreSQL Manager', fontsize=8, ha='center', color='white')
    
    ax.text(10, 7.6, 'Models & ORM', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(10, 7.0, '• User Model\n• Conversation Model\n• Connection Model\n• Health Check Model', fontsize=8, ha='center', color='white')
    
    ax.text(13.5, 7.6, 'Authentication', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(13.5, 7.0, '• Flask-Login\n• Session Management\n• User Roles', fontsize=8, ha='center', color='white')
    
    # AI Services Layer
    ai_box1 = FancyBboxPatch((1, 4.5), 6.5, 1.5, 
                             boxstyle="round,pad=0.1", 
                             facecolor=colors['ai'], 
                             alpha=0.7, edgecolor='black')
    ax.add_patch(ai_box1)
    ax.text(4.25, 5.9, 'AI Integration Layer', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(4.25, 5.5, 'Natural Language Processing', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(4.25, 4.85, '• Database Query Analysis\n• Action Detection\n• Intelligent Suggestions\n• Conversation Processing', fontsize=8, ha='center', color='white')
    
    # Database Connectivity Layer
    db_connect_box = FancyBboxPatch((8.5, 4.5), 6.5, 1.5, 
                                    boxstyle="round,pad=0.1", 
                                    facecolor=colors['external'], 
                                    alpha=0.7, edgecolor='black')
    ax.add_patch(db_connect_box)
    ax.text(11.75, 5.9, 'Database Connectivity Layer', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(10, 5.5, 'Multi-DB Support', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(10, 4.85, '• SQLite\n• PostgreSQL\n• MS SQL (pymssql)', fontsize=8, ha='center', color='white')
    ax.text(13.5, 5.5, 'Operations', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(13.5, 4.85, '• Health Checks\n• Space Analysis\n• Schema Analysis', fontsize=8, ha='center', color='white')
    
    # Data Storage Layer
    storage_box = FancyBboxPatch((1, 2), 14, 1.5, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor=colors['database'], 
                                 alpha=0.7, edgecolor='black')
    ax.add_patch(storage_box)
    ax.text(8, 3.4, 'Data Storage Layer', fontsize=14, fontweight='bold', ha='center', color='white')
    
    ax.text(3, 3.1, 'Application Database', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(3, 2.5, 'PostgreSQL\n• Users & Sessions\n• Conversations\n• Connection Configs', fontsize=8, ha='center', color='white')
    
    ax.text(8, 3.1, 'Target Databases', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(8, 2.5, 'Multi-Database Support\n• Production Systems\n• Development Environments', fontsize=8, ha='center', color='white')
    
    ax.text(13, 3.1, 'File Storage', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(13, 2.5, 'Local Storage\n• Reports (.txt)\n• Logs\n• Uploads', fontsize=8, ha='center', color='white')
    
    # External Systems (narrower box)
    external_box = FancyBboxPatch((1, 0.2), 9, 1, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor=colors['external'], 
                                  alpha=0.5, edgecolor='black')
    ax.add_patch(external_box)
    ax.text(5.5, 0.8, 'External Systems', fontsize=12, fontweight='bold', ha='center')
    ax.text(3, 0.5, 'Cloud Services', fontsize=10, ha='center')
    ax.text(5.5, 0.5, 'Database Servers', fontsize=10, ha='center')
    ax.text(8, 0.5, 'File System', fontsize=10, ha='center')
    
    # Add connection arrows
    # Frontend to Backend
    arrow1 = ConnectionPatch((8, 9), (8, 8.5), "data", "data",
                            arrowstyle="->", shrinkA=5, shrinkB=5, 
                            mutation_scale=20, fc=colors['connection'])
    ax.add_patch(arrow1)
    
    # Backend to AI Services
    arrow2 = ConnectionPatch((6, 6.5), (4.25, 6), "data", "data",
                            arrowstyle="->", shrinkA=5, shrinkB=5, 
                            mutation_scale=20, fc=colors['connection'])
    ax.add_patch(arrow2)
    
    # Backend to Database Connectivity
    arrow3 = ConnectionPatch((10, 6.5), (11.75, 6), "data", "data",
                            arrowstyle="->", shrinkA=5, shrinkB=5, 
                            mutation_scale=20, fc=colors['connection'])
    ax.add_patch(arrow3)
    
    # Services to Storage
    arrow4 = ConnectionPatch((8, 4.5), (8, 3.5), "data", "data",
                            arrowstyle="->", shrinkA=5, shrinkB=5, 
                            mutation_scale=20, fc=colors['connection'])
    ax.add_patch(arrow4)
    
    # Storage to External
    arrow5 = ConnectionPatch((8, 2), (8, 1.2), "data", "data",
                            arrowstyle="->", shrinkA=5, shrinkB=5, 
                            mutation_scale=20, fc=colors['connection'])
    ax.add_patch(arrow5)
    
    # Add data flow annotations
    ax.text(8.5, 8.75, 'HTTP Requests', fontsize=8, ha='left', style='italic')
    ax.text(4.5, 6.25, 'AI Processing', fontsize=8, ha='left', style='italic')
    ax.text(11, 6.25, 'DB Operations', fontsize=8, ha='left', style='italic')
    ax.text(8.5, 3.75, 'Data Queries', fontsize=8, ha='left', style='italic')
    ax.text(8.5, 1.6, 'External Calls', fontsize=8, ha='left', style='italic')
    
    # Add legend (moved to right side)
    legend_x, legend_y = 10.5, 0.2
    ax.text(legend_x, legend_y + 0.8, 'Legend:', fontsize=10, fontweight='bold')
    
    # Legend items
    legend_items = [
        (colors['frontend'], 'Frontend Layer'),
        (colors['backend'], 'Backend Services'),
        (colors['ai'], 'AI Integration'),
        (colors['external'], 'External/Connectivity'),
        (colors['database'], 'Data Storage')
    ]
    
    for i, (color, label) in enumerate(legend_items):
        y_pos = legend_y + 0.6 - (i * 0.12)
        legend_patch = patches.Rectangle((legend_x, y_pos), 0.2, 0.08, 
                                       facecolor=color, alpha=0.7, edgecolor='black')
        ax.add_patch(legend_patch)
        ax.text(legend_x + 0.25, y_pos + 0.04, label, fontsize=8, va='center')
    
    # Add technical details box (right edge aligned with Data Storage Layer box)
    tech_box = FancyBboxPatch((12.5, 0.3), 2.5, 1.5, 
                              boxstyle="round,pad=0.05", 
                              facecolor='lightgray', 
                              alpha=0.8, edgecolor='black')
    ax.add_patch(tech_box)
    ax.text(13.75, 1.65, 'Key Technologies', fontsize=9, fontweight='bold', ha='center')
    tech_details = [
        '• Flask Framework',
        '• SQLAlchemy ORM',
        '• Bootstrap 5 UI',
        '• Natural Language AI',
        '• Multi-DB Support',
        '• PostgreSQL',
        '• pymssql Connector'
    ]
    for i, detail in enumerate(tech_details):
        ax.text(12.6, 1.45 - (i * 0.15), detail, fontsize=7, ha='left')
    
    plt.tight_layout()
    return fig

def save_architecture_pdf():
    """Save the architecture diagram as PDF"""
    fig = create_architecture_diagram()
    
    # Save as PDF with high quality
    plt.savefig('vibe_system_architecture.pdf', 
                format='pdf', 
                dpi=300, 
                bbox_inches='tight',
                facecolor='white',
                edgecolor='none')
    
    print("✅ System architecture diagram created: vibe_system_architecture.pdf")
    print("📊 Diagram includes:")
    print("   - Frontend Layer (Bootstrap 5 UI)")
    print("   - Backend Services (Flask)")
    print("   - AI Integration (Natural Language Processing)")
    print("   - Database Connectivity (Multi-DB Support)")
    print("   - Data Storage Layer (PostgreSQL)")
    print("   - External Systems")
    print("   - Data flow arrows and technical details")
    
    plt.close()

if __name__ == "__main__":
    save_architecture_pdf()