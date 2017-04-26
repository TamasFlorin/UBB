#pragma once

#include <string>
#include <stdexcept>

class GraphException : public std::runtime_error
{
public:
	GraphException(std::string const &message) : std::runtime_error(message + " was thrown.")
	{
	}
};
