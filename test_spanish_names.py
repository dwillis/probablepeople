#!/usr/bin/env python
"""Test script for Spanish names and honorific titles."""

import probablepeople as pp

# Test cases
test_cases = [
    # The user's specific example
    "The Honorable James A. Rea, PhD",

    # Multi-word honorific titles
    "The Honorable Maria Rodriguez",
    "Hon. John D. Smith",
    "The Hon. Elizabeth Warren",
    "The Reverend Martin Luther King Jr.",
    "The Right Honorable David Cameron",

    # Academic and professional suffixes
    "Robert J. Williams, PhD",
    "Sarah Johnson, M.D.",
    "Michael P. Chen, Ph.D., MD",
    "Jennifer Taylor, D.O.",
    "Thomas R. Anderson, DDS",

    # Spanish titles
    "Don Carlos Mendoza",
    "Doña Isabel Ramirez",
    "Lic. Roberto Fernández",
    "Licenciado Miguel Hernández",
    "Ing. José Luis Torres",
    "Ingeniero Pedro Sánchez",
    "Dr. Juan González",

    # Double surnames (Spanish convention)
    "José García López",
    "María Carmen Rodríguez Martínez",
    "Juan Carlos Pérez Gómez",

    # Spanish name particles
    "María de la Cruz",
    "Juan del Carmen",
    "Carmen de los Ángeles",
    "Rosa de las Nieves",
    "Pedro de la Torre",
    "Miguel de León",

    # Complex Spanish names
    "Don Luis Miguel Vázquez Torres",
    "Doña Carmen Morales Jiménez",
    "Lic. Alberto Reyes Castro",
    "Ing. Roberto Carlos Mendoza Ruiz",
    "Dr. Fernando Álvarez González",

    # Modern South American names
    "Sofía Navarro Campos",
    "Valentina Ortiz Salazar",
    "Sebastián Moreno Rojas",
    "Camila Ramírez Vargas",
]

print("=" * 80)
print("Testing Spanish Names and Honorific Titles")
print("=" * 80)
print()

for name in test_cases:
    print(f"Input: {name}")
    try:
        result = pp.tag(name)
        parsed = pp.parse(name)
        print(f"  Tagged: {result[0]}")
        print(f"  Type: {result[1]}")
        print(f"  Parsed: {parsed}")
    except Exception as e:
        print(f"  ERROR: {e}")
    print()

print("=" * 80)
print("Testing complete!")
print("=" * 80)
