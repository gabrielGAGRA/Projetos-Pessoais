using Dapper;
using System.Data.SqlClient;
using backend.Domain.Entities;
using backend.Domain.Interfaces;

namespace backend.Infrastructure.Repositories
{
    public class QuotationRepository : IQuotationRepository
    {
        private readonly string _connectionString;

        public QuotationRepository(string connectionString)
        {
            _connectionString = connectionString;
        }

        public async Task<Quotation> GetQuotationAsync(string currencyFrom, string currencyTo)
        {
            using (var connection = new SqlConnection(_connectionString))
            {
                var sql = "SELECT TOP 1 * FROM Quotations WHERE CurrencyFrom = @CurrencyFrom AND CurrencyTo = @CurrencyTo ORDER BY Date DESC";
                return await connection.QueryFirstOrDefaultAsync<Quotation>(sql, new { CurrencyFrom = currencyFrom, CurrencyTo = currencyTo });
            }
        }
    }
}